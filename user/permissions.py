from rest_framework.permissions import IsAdminUser

from user.models import Types


class IsSuperAdminUser(IsAdminUser):
    """
    Allows access only to super admin users.
    """

    def has_permission(self, request, view):
        try:
            return bool(request.user and (request.user.type == Types.SUPERADMIN or request.user.is_superuser))
        except Exception:
            pass
        return bool(request.user and request.user.is_superuser)


class IsAdminUser(IsAdminUser):
    """
    Allows access only to admin users.
    """

    def has_permission(self, request, view):
        try:
            return bool(request.user and (request.user.type == Types.ADMIN or request.user.is_superuser))
        except Exception:
            pass
        return bool(request.user and request.user.is_superuser)


class IsOrdinaryUser(IsAdminUser):
    """
    Allows access only to ordinary users.
    """

    def has_permission(self, request, view):
        try:
            return bool(request.user and (request.user.type == Types.ORDINARY or request.user.is_superuser))
        except Exception:
            pass
        return bool(request.user and request.user.is_superuser)
