from .helpers import get_filename
from django.template.defaultfilters import slugify
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
User = get_user_model()
# Create your models here.

class Channel(models.Model):
    name = models.CharField(max_length=50)
    members = models.ManyToManyField(User,blank=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name='owned_channel')
    def get_absolute_url(self):
        return reverse('channel-detail',kwargs={'pk':self.pk})
    

class Post(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=1000)
    channel = models.ForeignKey(Channel,on_delete=models.CASCADE)
    body = models.TextField(max_length=10000,blank=True,null=True)
    score = models.PositiveIntegerField(default=0)
    
    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})



class File(models.Model):
    file = models.FileField(upload_to=get_filename)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)


class Comment(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    score = models.PositiveIntegerField(default=0)
    body = models.TextField(max_length=1000,blank=True,null=True)




