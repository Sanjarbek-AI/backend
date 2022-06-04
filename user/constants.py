from django.db import models


class Types(models.IntegerChoices):
    ADMIN = 0
    ORDINARY = 1
    SUPERUSER = 2


class GenderTypes(models.IntegerChoices):
    MALE = 0
    FEMALE = 1


class UserStatus(models.IntegerChoices):
    ACTIVE = 1
    INACTIVE = 0
    DELETED = -1
