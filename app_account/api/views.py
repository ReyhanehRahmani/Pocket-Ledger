import jwt
from datetime import datetime, timedelta
from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.throttling import AnonRateThrottle
from rest_framework_simplejwt.tokens import RefreshToken
from app_email.utils import send_templated_email
from app_account.models import EmailOTP
from app_account.api.serializers import EmailSerializer, UserRegistrationSerializer
MAX_OTP_ATTEMPTS = 15
TOKEN_TTL_MINUTES = 5


class OTPSendThrottle(AnonRateThrottle):
    scope = "otp_send"  # settings.py -> DEFAULT_THROTTLE_RATES["otp_send"] = "5/hour"


class OTPVerifyThrottle(AnonRateThrottle):
    scope = "otp_verify"  # settings.py -> DEFAULT_THROTTLE_RATES["otp_verify"] = "10/hour"


def make_verification_token(email, purpose="registration"):
    return jwt.encode(
        {
            "email": email,
            "purpose": purpose,
            "exp": datetime.utcnow() + timedelta(minutes=TOKEN_TTL_MINUTES),
        },
        settings.SECRET_KEY,
        algorithm="HS256",
    )


def read_verification_token(token, expected_purpose="registration"):
    """توکن رو باز می‌کنه و ایمیل رو برمی‌گردونه، یا خطای Response در صورت نامعتبر بودن."""
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        return None, Response({"detail": "توکن منقضی شده است. دوباره کد تایید بگیرید."}, status=400)
    except jwt.InvalidTokenError:
        return None, Response({"detail": "توکن نامعتبر است."}, status=400)

    if payload.get("purpose") != expected_purpose or not payload.get("email"):
        return None, Response({"detail": "توکن نامعتبر است."}, status=400)

    return payload["email"], None


class SendEmailOTPView(APIView):
    """ارسال کد تایید به ایمیل — هم برای ثبت‌نام و هم برای بازیابی رمز عبور (با فیلد purpose)"""
    permission_classes = [AllowAny]
    throttle_classes = [OTPSendThrottle]

    def post(self, request):
        serializer = EmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data["email"]
        purpose = request.data.get("purpose", "registration")

        user_exists = User.objects.filter(email=email).exists()
        if purpose == "registration" and user_exists:
            return Response({"detail": "کاربری با این ایمیل قبلاً ثبت‌نام کرده است. وارد شوید."}, status=400)
        if purpose == "password_reset" and not user_exists:
            return Response({"detail": "کاربری با این ایمیل یافت نشد."}, status=404)

        existing = EmailOTP.objects.filter(email=email).first()

        if purpose == "registration" and existing and existing.is_verified:
            return Response({"detail": "این ایمیل قبلاً تایید شده است."}, status=400)

        if existing and not existing.is_verified and not existing.is_expired():
            remaining = int((existing.created_at + timedelta(minutes=2) - timezone.now()).total_seconds())
            
            return Response(
                {"detail": f"کد قبلی هنوز معتبر است. {remaining} ثانیه دیگر تلاش کنید.",
                 "remaining_seconds": remaining},
                status=429,
            )

        otp_instance = EmailOTP.create_otp(email)
        subject = "کد بازیابی رمز عبور" if purpose == "password_reset" else "کد تایید ورود"

        if not send_templated_email(
            subject=subject,
            template_name="otp.html",
            context={"otp_code": otp_instance.otp_code},
            recipient_list=[email],
        ):
            return Response({"detail": "ارسال ایمیل با خطا مواجه شد."}, status=500)

        return Response({"detail": "کد تایید به ایمیل شما ارسال شد.", "email": email}, status=200)


class VerifyOTPView(APIView):
    """تایید کد OTP و برگرداندن توکن موقت برای مرحله بعد (purpose مشخص می‌کند توکن برای ثبت‌نام است یا بازیابی رمز)"""
    permission_classes = [AllowAny]
    throttle_classes = [OTPVerifyThrottle]

    def post(self, request):
        otp_code = request.data.get("otp_code")
        email = (request.data.get("email") or "").strip().lower()
        purpose = request.data.get("purpose", "registration")

        if not otp_code or not email:
            return Response({"detail": "ایمیل و کد تایید الزامی هستند."}, status=400)

        otp_instance = EmailOTP.objects.filter(email=email).first()
        if not otp_instance:
            return Response({"detail": "ایمیل یافت نشد."}, status=404)

        if otp_instance.is_expired():
            return Response({"detail": "کد تایید منقضی شده است."}, status=400)

        if otp_instance.attempts >= MAX_OTP_ATTEMPTS:
            return Response({"detail": "تعداد تلاش‌های مجاز به پایان رسید. کد جدید درخواست کنید."}, status=429)

        if otp_instance.otp_code != otp_code:
            otp_instance.attempts += 1
            otp_instance.save(update_fields=["attempts"])
            return Response({"detail": "کد تایید اشتباه است."}, status=400)

        otp_instance.is_verified = True
        otp_instance.save(update_fields=["is_verified"])

        return Response({
            "status": "ok",
            "message": "کد تایید شد.",
            "verification_token": make_verification_token(email, purpose=purpose),
            "email": email,
        }, status=200)
    

class UserRegistrationView(APIView):
    """ساخت کاربر جدید با توکن تایید"""
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data["username"]
        password = serializer.validated_data["password"]

        email, error = read_verification_token(serializer.validated_data["verification_token"])
        if error:
            return error

        if User.objects.filter(email=email).exists():
            return Response({"detail": "کاربری با این ایمیل قبلاً ثبت‌نام کرده است."}, status=400)

        user = User.objects.create_user(username=username, password=password, email=email)
        EmailOTP.objects.filter(email=email).delete()  # پاک‌سازی OTP مصرف‌شده

        refresh = RefreshToken.for_user(user)
        return Response({
            "status": "ok",
            "message": "کاربر با موفقیت ساخته شد.",
            "user_id": user.id,
            "username": user.username,
            "access": str(refresh.access_token),
            "refresh": str(refresh),
        }, status=200)
    

class ResetPasswordView(APIView):
    """تنظیم رمز عبور جدید با استفاده از توکن موقت بازیابی"""
    permission_classes = [AllowAny]

    def post(self, request):
        verification_token = request.data.get("verification_token")
        new_password = request.data.get("new_password")

        if not verification_token or not new_password:
            return Response({"detail": "توکن و رمز عبور جدید الزامی هستند."}, status=400)

        if len(new_password) < 8:
            return Response({"detail": "رمز عبور باید حداقل ۸ کاراکتر باشد."}, status=400)

        email, error = read_verification_token(verification_token, expected_purpose="password_reset")
        if error:
            return error

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({"detail": "کاربری با این ایمیل یافت نشد."}, status=404)

        user.set_password(new_password)
        user.save(update_fields=["password"])
        EmailOTP.objects.filter(email=email).delete()

        return Response({"detail": "رمز عبور با موفقیت تغییر کرد."}, status=200)