import random
from datetime import timedelta

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class EmailOTP(models.Model):

    """مدل OTP برای ایمیل"""

    email = models.EmailField(unique=True)
    otp_code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)
    attempts = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f"{self.email} - {self.otp_code}"

    def is_expired(self):
        expiration_time = self.created_at + timedelta(minutes=2)
        return timezone.now() > expiration_time

    @classmethod
    def generate_otp(cls):
        return str(random.randint(100000, 999999))

    @classmethod
    def create_otp(cls, email):
        email = email.strip().lower()
        otp_code = cls.generate_otp()
        cls.objects.filter(email=email).delete()
        return cls.objects.create(
            email=email,
            otp_code=otp_code)