from rest_framework import serializers
from django.contrib.auth.models import User

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