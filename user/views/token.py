from rest_framework_simplejwt.views import TokenObtainPairView
from user.serializers.token import MyTokenObtainPairSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    """View for generating JWT token"""
    serializer_class = MyTokenObtainPairSerializer
