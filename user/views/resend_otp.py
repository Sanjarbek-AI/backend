import time

from drf_spectacular.utils import extend_schema
from rest_framework import views
from rest_framework.authentication import SessionAuthentication
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from user.models import UserModel
from user.serializers.resend_otp import ResendOtpSerializer
from utils.language import LanguageDetector
from utils.phone_validation import phone_validation
from utils.send_otp import generateKey
from utils.send_otp import send_sms


class CsrfExemptSessionAuthentication(SessionAuthentication):
    """Class to remove Csrf token from the request"""

    def enforce_csrf(self, request):
        return


class ResendOtpView(views.APIView, LanguageDetector):
    """Class to resend OTP through SMS"""
    serializer_class = ResendOtpSerializer
    permission_classes = (AllowAny,)

    @extend_schema(
        operation_id="user",
        tags=["user"]
    )
    def post(self, request, *args, **kwargs):
        """Function for checking user existence and resending OTP"""
        serializer = ResendOtpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data

        # validation
        phone_number = validated_data.get('phone_number')
        phone_number = phone_validation(phone_number)

        response_data = dict()

        try:
            user = UserModel.objects.get(phone_number=phone_number)
        except UserModel.DoesNotExist:
            response_data['success'] = False
            response_data['detail'] = self.get_response_message('user_not_found')
            return Response(response_data, status=404)

        # """ Just for test purposes. Delete after the test is finished, because this part """
        # """ is identical with the part below. """"""""""""""""""""""""""""""""""""""""""""""
        if user.phone_number == "+998123334455":
            if user.time_otp is None:
                user.otp_key = "111111"
                user.time_otp = time.time()
                user.save()
                otp_key = "111111"
                response_data['success'] = True
                response_data['detail'] = 'OTP sent successfully'
                response_data['resend_time'] = 120
                response_data['user_phone_number'] = str(user)
                return Response(response_data, status=200)
            else:
                cur_time = time.time()
                res_time = cur_time - float(user.time_otp)
                if res_time <= 120:
                    response_data['success'] = False
                    secns = int(120 - res_time)
                    minutes = str((secns % 3600) // 60)
                    seconds = str((secns % 3600) % 60)
                    response_data['detail'] = self.get_response_message('otp_already_sent').format(minutes, seconds)
                    return Response(response_data, status=400)
                user.otp_key = "111111"
                user.time_otp = time.time()
                user.save()
                otp_key = "111111"
                response_data['success'] = True
                response_data['detail'] = 'OTP sent successfully'
                response_data['resend_time'] = 120
                response_data['user_phone_number'] = str(user)
                return Response(response_data, status=200)
        # """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

        if user.time_otp is None:
            key = generateKey.returnValue()
            user.otp_key = key['OTP']
            user.save()
            otp_key = key['OTP']
            if send_sms(user, otp_key) == 200:
                response_data['success'] = True
                response_data['detail'] = 'OTP sent successfully'
                response_data['resend_time'] = 120
                response_data['user_phone_number'] = str(user)
                return Response(response_data, status=200)
            else:
                raise ValidationError('Error in sending OTP')
        else:
            cur_time = time.time()
            res_time = cur_time - float(user.time_otp)
            if res_time <= 120:
                response_data['success'] = False
                secns = int(120 - res_time)
                minutes = str((secns % 3600) // 60)
                seconds = str((secns % 3600) % 60)
                response_data['detail'] = self.get_response_message('otp_already_sent').format(minutes, seconds)
                return Response(response_data, status=400)
            key = generateKey.returnValue()
            user.otp_key = key['OTP']
            user.save()
            otp_key = key['OTP']
            if send_sms(user, otp_key) == 200:
                response_data['success'] = True
                response_data['detail'] = 'OTP sent successfully'
                response_data['resend_time'] = 120
                response_data['user_phone_number'] = str(user)
                return Response(response_data, status=200)
            else:
                raise ValidationError('Error in sending OTP')
