from django.contrib.auth.models import User
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed


class HeaderUserAuthentication(BaseAuthentication):
    def authenticate(self, request):
        user_id = request.headers.get("X-User-Id")
        if not user_id:
            return None

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise AuthenticationFailed("User not found")

        return (user, None)