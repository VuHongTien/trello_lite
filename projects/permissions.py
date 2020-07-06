from rest_framework.permissions import BasePermission
from django.contrib.auth.models import AnonymousUser


class UserPermission(BasePermission):
    def has_permission(self, request, view):
        current_user = request.user
        return True if type(current_user) is not AnonymousUser else False
