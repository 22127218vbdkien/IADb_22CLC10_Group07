from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from rest_framework.response import Response

class IsOwnerPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        try:
            return obj.user_id == request.user
        except:
            return obj.owner_id == request.user