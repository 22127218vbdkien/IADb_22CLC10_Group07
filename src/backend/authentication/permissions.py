from rest_framework import permissions
from django.contrib.auth.models import User
class IsOwnerPermission(permissions.BasePermission):
    """
    Object-level permission to only allow updating his own profile
    """
    def has_object_permission(self, request, view, obj):
        return obj == request.user
