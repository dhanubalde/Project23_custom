from .models import CustomUser
from rest_framework import serializers

class CustomUserSerialiser(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'id',
            'name',
            'address',
            'contact',
            'email'
        ]
    def get_my_user_data(self, obj):
        return {
            'username': obj.user.username,
        }