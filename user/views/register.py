from django.db import IntegrityError
from drf_spectacular.utils import extend_schema
from rest_framework import views
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from user.models import UserModel, Types, UserStatus
from user.serializers.register import RegisterSerializer
from utils.gender_validation import validate_gender
from utils.language import LanguageDetector
from utils.phone_validation import phone_validation
from utils.send_otp import generateKey, send_sms


class CsrfExemptSessionAuthentication(SessionAuthentication):
    """Class to remove Csrf token from the request"""

    def enforce_csrf(self, request):
        return


class RegisterView(views.APIView, LanguageDetector):
    """Class to send register a user"""
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)

    @extend_schema(
        operation_id="user",
        tags=["user"]
    )
    def post(self, request, *args, **kwargs):
        """Validate a user and create"""
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data

        # validation
        response_data = dict()
        phone_number = validated_data.get('phone_number')
        phone_number = phone_validation(phone_number)

        try:
            user = UserModel.objects.create_user(phone_number=phone_number,
                                                 first_name=validated_data['first_name'],
                                                 last_name=validated_data['last_name'],
                                                 type=Types.ORDINARY)
        except IntegrityError:
            response_data['success'] = False
            response_data['detail'] = self.get_response_message('number_exists')
            return Response(response_data, status=400)

        if user:
            key = generateKey.returnValue()
            user.otp_key = key['OTP']
            user.save()
            otp_key = key['OTP']
            if send_sms(user, otp_key) == 200:
                user.save()
                response_data['success'] = True
                response_data['detail'] = 'OTP sent successfully.'
                response_data['resend_time'] = 120
                response_data['user_phone_number'] = str(user.phone_number)
                return Response(response_data, status=201)
            else:
                response_data['success'] = False
                response_data['detail'] = self.get_response_message('send_otp_error')
                return Response(response_data, status=400)
        else:
            response_data['success'] = False
            response_data['detail'] = "Not ok"
            return Response(response_data, status=404)
