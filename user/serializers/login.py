from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    """Serializer for Login View"""
    phone_number = serializers.CharField()
