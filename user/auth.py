from datetime import timedelta

from django.http.response import Http404
from rest_framework_simplejwt.tokens import RefreshToken

from user.models import UserModel


class PhoneAuthBackend:
    """Custom backend for validating user throught phone number"""

    def authenticate(self, request=None, phone_number=None):
        """Custom function to authenticate a user"""
        try:
            user = UserModel.objects.get(phone_number=phone_number)
        except (UserModel.DoesNotExist, Http404):
            return None

        return user

    def get_user(self, user_id):
        try:
            return UserModel.objects.get(id=user_id)
        except UserModel.DoesNotExist:
            return None


class EmailAuthBackend:
    """Custom backend for validating user throught email address"""

    def authenticate(self, request=None, email=None, password=None):
        """Custom function to authenticate a user"""
        try:
            user = UserModel.objects.get(email=email)
            if user.check_password(password) is True:
                return user
        except (UserModel.DoesNotExist, Http404):
            return None

    def get_user(self, user_id):
        try:
            return UserModel.objects.get(id=user_id)
        except UserModel.DoesNotExist:
            return None


def generate_user_tokens(user):
    """Function for generating JWT"""
    refresh_token = RefreshToken.for_user(user)
    refresh_token['user_role'] = user.type
    refresh_token['user_id'] = user.id
    access_token = refresh_token.access_token

    response = dict()
    response["refresh_token"] = str(refresh_token)
    response["access_token"] = str(access_token)
    return response


def generate_admin_user_tokens(user, remember_me):
    """Function for generating JWT"""
    refresh_token = RefreshToken.for_user(user)
    refresh_token['user_role'] = user.type
    refresh_token['user_id'] = user.id
    if remember_me == True:
        refresh_token.set_exp(lifetime=timedelta(days=7))
        access_token = refresh_token.access_token
        access_token.set_exp(lifetime=timedelta(days=1))
        # refresh_token.set_exp(lifetime=timedelta(minutes=7))
        # access_token = refresh_token.access_token
        # access_token.set_exp(lifetime=timedelta(minutes=2))
    else:
        refresh_token.set_exp(lifetime=timedelta(days=2))
        access_token = refresh_token.access_token
        access_token.set_exp(lifetime=timedelta(days=1))
        # refresh_token.set_exp(lifetime=timedelta(minutes=4))
        # access_token = refresh_token.access_token
        # access_token.set_exp(lifetime=timedelta(minutes=2))

    response = dict()
    response["refresh_token"] = str(refresh_token)
    response["access_token"] = str(access_token)
    return response
