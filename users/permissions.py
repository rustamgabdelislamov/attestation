from rest_framework import permissions


class IsActivePermission(permissions.BasePermission):
    message = "Только активные сотрудники имеют доступ."

    def has_permission(self, request, view):
        if hasattr(request.user, "is_active"):
            return request.user.is_active
        else:
            return False
