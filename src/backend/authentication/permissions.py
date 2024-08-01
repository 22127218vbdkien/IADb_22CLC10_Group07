from rest_framework import permissions
from django.contrib.auth.models import User
class IsOwnerPermission(permissions.BasePermission):
    """
    Object-level permission to only allow updating his own profile
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if isinstance(obj, User):
            return obj == request.user
        return obj.user == request.user
