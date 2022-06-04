from rest_framework import serializers


class VerifySmsSerializer(serializers.Serializer):
    """Serializer for Verify SMS View"""
    phone_number = serializers.CharField()
    otp_key = serializers.CharField()
