from rest_framework import serializers


class ResendOtpSerializer(serializers.Serializer):
    """Serializer for Resend OTP View"""
    phone_number = serializers.CharField()
