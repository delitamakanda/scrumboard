from rest_framework import permissions

class IsUserOfPost(permissions.BasePermission):
    """docstring for IsUserOfPost."""
    def has_object_permission(self, request, view, list):
        if request.user:
            return list.user == request.user
        return False
