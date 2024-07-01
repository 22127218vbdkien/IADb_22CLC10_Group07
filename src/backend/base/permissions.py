from rest_framework.permissions import BasePermission

class MyCustomPermission(BasePermission):
  """
  Custom permission logic here
  """

  def has_permission(self, request, view):
    # Implement your permission check logic here
    # Return True if permission is granted, False otherwise
    if request.method == 'GET':
      return True

    # For edit requests (PUT, PATCH, DELETE), check user permissions
    user = request.user
    if user.is_authenticated:
      if view.action in ('update', 'partial_update', 'destroy'):
        # Implement your edit permission logic here
        # This could involve checking user groups, roles, or specific permissions
        # Replace with your actual permission check
        return user.has_perm('app.change_anime')  # Replace 'app.change_anime' with your permission codename
    return False 

  def has_object_permission(self, request, view, obj):
    # Implement object-level permission check logic (optional)
    return True