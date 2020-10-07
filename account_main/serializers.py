from rest_framework import routers, serializers, viewsets
from .models import User

# Serializers define the API representation.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'user_id',
            'first_name',
            'last_name',
            'username',
            'birthday',
            'email',
            'password',
            'phone',
            'is_admin',
            'is_active',
            'avatar',
        ]
