from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL
# Create your models here.
class CustomUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    address = models.TextField( max_length=200, null=True, blank=True)
    contact = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200,null=True, blank=True)
    created = models.DateTimeField(auto_now=True)
    Updated = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    
