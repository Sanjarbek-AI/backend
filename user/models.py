from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from user.constants import Types, GenderTypes, UserStatus
from user.managers import UserManager


class UserModel(AbstractBaseUser, PermissionsMixin):
    """ Model to store User data"""
    type = models.SmallIntegerField(_("Type"), choices=Types.choices, default=Types.ORDINARY)
    is_superuser = models.BooleanField(default=False, verbose_name='Superuser')
    is_staff = models.BooleanField(default=False, verbose_name='Superuser')
    phone_number = models.CharField(max_length=13, unique=True, blank=True, null=True, verbose_name='Phone Number')
    email = models.EmailField(max_length=100, unique=True, blank=True, null=True, verbose_name='Email')
    first_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='First Name')
    last_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Last Name')
    profile_picture = models.ImageField(blank=True, null=True, verbose_name='Profile Picture')
    gender = models.SmallIntegerField(_('Gender Type'), choices=GenderTypes.choices, blank=True, null=True, default=1)
    country = models.CharField(max_length=255, blank=True, null=True, verbose_name='Country')
    city = models.CharField(max_length=255, blank=True, null=True, verbose_name='City')
    district = models.CharField(max_length=255, blank=True, null=True, verbose_name='District')
    street = models.CharField(max_length=255, blank=True, null=True, verbose_name='Street')
    house_number = models.CharField(max_length=255, blank=True, null=True, verbose_name='House Number')
    otp_key = models.CharField(max_length=24, blank=True, null=True, verbose_name='Otp Key')
    time_otp = models.BigIntegerField(blank=True, null=True, verbose_name='Time Otp')
    remember_me = models.BooleanField(default=False, verbose_name='Remember me')
    status = models.SmallIntegerField(choices=UserStatus.choices, default=UserStatus.INACTIVE, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'phone_number'
    EMAIL_USERNAME_FIELD = 'email'
    objects = UserManager()

    def __str__(self):
        return f"{self.first_name} | {self.last_name}"

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
