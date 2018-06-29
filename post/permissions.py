from rest_framework.permissions import IsAuthenticatedOrReadOnly, SAFE_METHODS
class IsOwnerOrReadOnly(IsAuthenticatedOrReadOnly):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.owner == request.user
