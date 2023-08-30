from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Post(models.Model):
    image=models.ImageField(upload_to='media', null=True, blank=True)
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    WEATHER_CHOICES = (
        ('0', '#맑음'),
        ('1', '#흐림'),
        ('2', '#비'),
        ('3', '#눈'),
        ('4', '#바람'),
    )
    weather=models.CharField(max_length=3, default=0, choices=WEATHER_CHOICES)
    weather_desc=models.CharField(max_length=100, null=True, blank=True)
    temp=models.CharField(max_length=5)
    temp_desc=models.CharField(max_length=100, null=True, blank=True)
    FINEDUST_CHOICES = (
        ('0', '#좋음'),
        ('1', '#조금좋음'),
        ('2', '#보통'),
        ('3', '#조금나쁨'),
        ('4', '#나쁨'),
    )
    finedust=models.CharField(max_length=4, default=0, choices=FINEDUST_CHOICES)
    finedust_desc=models.CharField(max_length=100, null=True, blank=True)
    tmi=models.TextField(null=True, blank=True)
    liked=models.IntegerField(null=True, blank=True)
    scrap=models.IntegerField(null=True, blank=True)
    wear_tag1=models.CharField(max_length=10)
    wear_tag2=models.CharField(max_length=10, null=True, blank=True)
    wear_tag3=models.CharField(max_length=10, null=True, blank=True)
    today_tag1=models.CharField(max_length=10)
    today_tag2=models.CharField(max_length=10, null=True, blank=True)
    today_tag3=models.CharField(max_length=10, null=True, blank=True)
    feel = models.CharField(max_length=10, null=True, blank=True,default = '')
    
    
class Scrap(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='scrap_user')
    post=models.ForeignKey(Post, on_delete=models.CASCADE, related_name='scrap_post')