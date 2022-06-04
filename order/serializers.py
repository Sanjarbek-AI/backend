from rest_framework import serializers


class OrderSerializer(serializers.Serializer):
    """Serializer to create an order"""
    data = serializers.ListField(child=serializers.DictField())
    description = serializers.CharField(max_length=255, required=False)
