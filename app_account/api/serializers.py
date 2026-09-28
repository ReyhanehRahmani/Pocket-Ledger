from rest_framework import serializers
from django.contrib.auth.models import User
from app_account.models import Profile


class EmailSerializer(serializers.Serializer):

    email = serializers.EmailField()

    def validate_email(self, value):
        return value.strip().lower()


class UserRegistrationSerializer(serializers.Serializer):
    
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(write_only=True, min_length=8)
    verification_token = serializers.CharField()

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("این نام کاربری قبلاً استفاده شده است.")
        return value
    


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", max_length=150, required=False)
    email = serializers.EmailField(source="user.email", read_only=True)
    date_joined = serializers.DateTimeField(source="user.date_joined", read_only=True)

    class Meta:
        model = Profile
        fields = ["avatar", "username", "email", "date_joined"]

    def validate_username(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError("نام کاربری نمی‌تواند خالی باشد.")
        taken = User.objects.filter(username__iexact=value).exclude(pk=self.instance.user.pk).exists()
        if taken:
            raise serializers.ValidationError("این نام کاربری قبلاً استفاده شده است.")
        return value

    def update(self, instance, validated_data):
        user_data = validated_data.pop("user", {})
        if "username" in user_data:
            instance.user.username = user_data["username"]
            instance.user.save(update_fields=["username"])
        return super().update(instance, validated_data)