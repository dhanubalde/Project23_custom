
from rest_framework import generics
from apps.serializers import CustomUserSerialiser
from .models import CustomUser

class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerialiser
    lookup_field = 'pk'
    
user_list_view = UserListCreateAPIView.as_view()


class UserDetailAPIView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerialiser
    lookup_field = 'pk'
    
user_detail_view = UserDetailAPIView.as_view()

class UserUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerialiser
    lookup_field = 'pk'
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
user_update_view = UserUpdateAPIView.as_view()

class UserDeleteAPIView(generics.RetrieveDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerialiser
    lookup_field = 'pk'
    

user_delete_view = UserDeleteAPIView.as_view()