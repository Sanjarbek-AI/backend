from django.contrib.auth.models import BaseUserManager

from user.constants import UserStatus
from user.models import Types
from utils.phone_validation import phone_validation


class UserManager(BaseUserManager):
    """Helps to create user(s), and to create super user(s) and etc."""

    def create_user(self, phone_number, **kwargs):
        """Create and return a user with username"""
        if not phone_number:
            raise ValueError('User must have a phone number.')

        user = self.model(phone_number=phone_number, **kwargs)
        user.save(using=self._db)
        return user

    def create_superadmin(self, phone_number, password, **kwargs):
        """Create and return a staffuser"""
        if not phone_number:
            raise ValueError('Superadminuser must have a phone number.')

        phone_number = phone_validation(phone_number)
        user = self.model(phone_number=phone_number, **kwargs)
        user.set_password(password)
        user.is_active = True
        user.type = Types.SUPERADMIN
        user.is_superuser = False
        user.save(using=self._db)

        return user

    def create_admin(self, phone_number, password, **kwargs):
        """Create and return a staffuser"""
        if not phone_number:
            raise ValueError('Adminuser must have a phone number.')

        user = self.model(phone_number=phone_number, **kwargs)
        user.set_password(password)
        user.is_active = True
        user.type = Types.ADMIN
        user.is_superuser = False
        user.save(using=self._db)

        return user

    def create_factoryadmin(self, phone_number, password, **kwargs):
        """Create and return a staffuser"""
        if not phone_number:
            raise ValueError('Superuser must have a phone number.')

        user = self.model(phone_number=phone_number, **kwargs)
        user.set_password(password)
        user.is_active = True
        user.type = Types.FACTORYADMIN
        user.is_staff = False
        user.is_superuser = False
        user.save(using=self._db)

        return user

    def create_superuser(self, phone_number, password):
        """Create and return a superuser"""
        if not phone_number:
            raise ValueError('Superuser must have a phone number.')

        user = self.model(phone_number=phone_number)
        user.set_password(password)
        user.status = UserStatus.ACTIVE
        user.type = Types.SUPERUSER
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user
