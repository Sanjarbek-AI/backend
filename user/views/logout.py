from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken, OutstandingToken, BlacklistedToken

from user.permissions import IsOrdinaryUser
from user.serializers.logout import LogoutSerializer
from utils.language import LanguageDetector


class LogoutView(APIView, LanguageDetector):
    """View to log out a user"""
    serializer_class = LogoutSerializer
    permission_classes = (AllowAny,)

    def get_object(self):
        return self.request.user

    @extend_schema(
        operation_id="user",
        tags=["user"]
    )
    def post(self, request, *args, **kwargs):
        """Get acquired refresh token and blacklist it"""
        try:
            serializer = LogoutSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            validated_data = serializer.validated_data
            refresh_token = validated_data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            response_data = dict()
            response_data['success'] = True
            response_data['detail'] = self.get_response_message('user_logged_out')
            return Response(response_data, status=200)
        except Exception as e:
            print(e)
            response_data = dict()
            response_data['success'] = False
            response_data['detail'] = self.get_response_message('token_blacklisted')
            return Response(response_data, 400)


class LogoutAllView(APIView, LanguageDetector):
    """View to log out a user"""
    permission_classes = (IsAuthenticated,)

    @extend_schema(
        operation_id="user",
        tags=["user"]
    )
    def post(self, request, *args, **kwargs):
        """Search refresh tokens associated with a specific user and blacklist them"""
        tokens = OutstandingToken.objects.filter(user_id=request.user.id)
        for token in tokens:
            token, _ = BlacklistedToken.objects.get_or_create(token=token)

        response_data = dict()
        response_data['success'] = True
        response_data['detail'] = self.get_response_message('logged_out_all_devices')
        return Response(response_data, status=200)
