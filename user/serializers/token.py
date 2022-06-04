from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from user.models import UserModel


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    """Serializer for Token generation View"""

    username_field = UserModel.EMAIL_USERNAME_FIELD

    @classmethod
    def get_token(cls, user: UserModel):
        token = super().get_token(user)

        token['user_role'] = user.type
        token['user_id'] = user.id
        return token
