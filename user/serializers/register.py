from rest_framework import serializers


class RegisterSerializer(serializers.Serializer):
    """Serializer for Register View"""
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    phone_number = serializers.CharField(required=True)
    # gender = serializers.IntegerField(required=True)
