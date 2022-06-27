from operator import mod
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=1000)
    body = models.TextField(max_length=10000,blank=True,null=True)
    score = models.PositiveIntegerField(default=0)
