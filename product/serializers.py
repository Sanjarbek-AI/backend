from rest_framework import serializers


class WishlistSerializer(serializers.Serializer):
    """Serializer to create an order"""
    product_id = serializers.IntegerField()
