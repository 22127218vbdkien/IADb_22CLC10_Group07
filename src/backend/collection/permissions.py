from rest_framework import permissions
from django.contrib.auth.models import User

class IsOwnerPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user_id == request.user