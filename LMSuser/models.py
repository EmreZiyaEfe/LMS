from django.db import models
from django.contrib.auth.models import AbstractUser

def get_default_profile_image():
    return 'profile_pic/avatar.png'

class CustomUser(AbstractUser):
    image = models.ImageField(upload_to='profile_pic', null=True, blank=True, default=get_default_profile_image, verbose_name='Profil Resmi')
    phone_number = models.CharField(max_length=11, null=True)
    tc = models.CharField(max_length=11, null=True)
    is_teacher = models.BooleanField(default=False)
    password = models.CharField(max_length=128) 


