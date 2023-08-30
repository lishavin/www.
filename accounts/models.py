from django.db import models
from django.contrib.auth.models import User, AbstractUser

class Users(AbstractUser):

    nickname = models.CharField(max_length=30, null=True,blank=True) # 닉네임
    user_image = models.ImageField(upload_to = 'images/', null= True, blank =True)
    introduction = models.TextField(blank = True)