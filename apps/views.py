
from rest_framework import generics
from apps.serializers import CustomUserSerialiser
from .models import CustomUser

class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerialiser
    lookup_field = 'pk'
    
user_list_view = UserListCreateAPIView.as_view()