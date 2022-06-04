from rest_framework import serializers


class LogoutSerializer(serializers.Serializer):
    """Serializer for Logout View"""
    refresh_token = serializers.CharField()
