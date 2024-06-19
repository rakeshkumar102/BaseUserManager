from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,PermissionsMixin
# Create your models here.

class UserProfileManager(BaseUserManager):
    def create_user(self,email,first_name,last_name,password=None):
        if not email:
            raise ValueError('email not provided')
        nE=self.normalize_email(email)
        UO=self.model(email=nE,first_name=first_name,last_name=last_name)
        UO.set_password(password)
        UO.save()
        return UO

    def create_superuser(self,email,first_name,last_name,password):
        UO=self.create_user(email,first_name,last_name,password)
        UO.is_staff=True
        UO.is_superuser=True
        UO.save() 

class UserProfile(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(primary_key=True)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['first_name','last_name']

    objects=UserProfileManager()


