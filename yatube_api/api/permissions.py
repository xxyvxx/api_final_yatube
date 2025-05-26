from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Разрешаем GET, HEAD, OPTIONS для всех
        # POST только для аутентифицированных
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Разрешаем GET, HEAD, OPTIONS для всех
        # PUT, PATCH, DELETE только для автора
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
