from rest_framework import serializers
from .models import UserProfile, Messages
from django.contrib.auth.models import User


class UsersSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_login'
        )

class UserProfileSerializer(serializers.ModelSerializer):

    user = UsersSerializer()

    class Meta:
        model = UserProfile
        fields = "__all__"


