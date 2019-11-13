from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsUserOfPost(BasePermission):
    """docstring for IsUserOfPost."""
    def has_object_permission(self, request, view, list):
        if request.user:
            return list.user == request.user
        return False



class IsAdminUser(BasePermission):
    """
    Allows access only to admin users.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_staff


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        else:
            return request.user.is_staff
