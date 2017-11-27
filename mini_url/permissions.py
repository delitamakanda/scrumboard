from rest_framework import permissions

class IsUserOfPost(permissions.BasePermission):
    """docstring for IsUserOfPost."""
    def has_object_permission(self, request, view, list):
        if request.user:
            return list.user == request.user
        return False
    
    
    
class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.owner == request.user
    
    
    
class IsAdminUser(permissions.BasePermission):
    """
    Allows access only to admin users.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_staff
