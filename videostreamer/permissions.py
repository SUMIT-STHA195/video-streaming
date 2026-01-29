from rest_framework import permissions

class IsCreator(permissions.BasePermission):
    def has_permission(self, request, view):
        # Initial check: Is the user logged in and registered as a creator?
        return bool(request.user and request.user.is_authenticated and request.user.is_creator)

    def has_object_permission(self, request, view, obj):
        # Checks if the video's creator is the user making the request
        # This prevents User A from deleting User B's video
        return obj.creator == request.user