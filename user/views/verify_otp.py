import time

from drf_spectacular.utils import extend_schema
from rest_framework import permissions
from rest_framework import views
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response

from user.auth import generate_user_tokens
from user.models import UserStatus, UserModel
from user.serializers.verify_otp import VerifySmsSerializer
from utils.language import LanguageDetector


class CsrfExemptSessionAuthentication(SessionAuthentication):
    """Class to remove Csrf token from the request"""

    def enforce_csrf(self, request):
        return


class VerifyOTPView(views.APIView, LanguageDetector):
    """Class to verifty an OTP send though SMS"""
    serializer_class = VerifySmsSerializer
    # authentication_classes = (CsrfExemptSessionAuthentication,)
    permission_classes = (permissions.AllowAny,)

    @extend_schema(
        tags=["user"]
    )
    def post(self, request):
        """Verify an OTP and login a user"""
        serializer = VerifySmsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data

        phone_number = validated_data.get('phone_number')

        code = validated_data.get('otp_key')

        if phone_number and code:
            response_data = dict()

            try:
                user = UserModel.objects.get(phone_number=phone_number)
            except UserModel.DoesNotExist:
                response_data['status'] = False
                response_data['detail'] = self.get_response_message('number_does_not_exist')
                return Response(response_data, status=400)

            if user.otp_key is None:
                response_data['status'] = False
                response_data['detail'] = self.get_response_message('code_is_used')
                return Response(response_data, status=400)
            else:
                # user = authenticate(phone_number=user.phone_number)
                if user:
                    time_otp = user.time_otp
                    now = time.time()
                    res = now - float(time_otp)
                    if user.otp_key == code and res <= 120:
                        user.time_otp = None
                        user.status = UserStatus.ACTIVE
                        user.otp_key = None
                        user.save()
                        tokens = generate_user_tokens(user)
                        response_data['success'] = True
                        response_data['user_id'] = user.id
                        response_data['phone_number'] = user.phone_number
                        response_data['first_name'] = user.first_name
                        response_data['last_name'] = user.last_name
                        response_data['status'] = user.status
                        response_data['detail'] = self.get_response_message('number_verified')
                        response_data['token'] = {
                            'access_token': tokens['access_token'],
                            'refresh_token': tokens['refresh_token']
                        }
                        return Response(response_data, status=200)
                    else:
                        user.status = UserStatus.INACTIVE
                        user.save()
                        response_data['success'] = False
                        response_data['detail'] = self.get_response_message('invalid_code')
                        return Response(response_data, status=400)
                else:
                    response_data['success'] = False
                    response_data['detail'] = self.get_response_message('user_not_found')
                    return Response(response_data, status=404)
