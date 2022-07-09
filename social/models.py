from .helpers import get_filename
import imghdr
from PIL import Image
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
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        path = self.file.path
        if imghdr.what(path):
            print(f'compressing image {path}')
            image = Image.open(path)
            image.save(path,quality=60,optimize=True)
        else:
            print('Not an image, therefore not compressing')
    
    @property
    def root_folder(self):
        return 'post_files/'


class Comment(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    score = models.PositiveIntegerField(default=0)
    body = models.TextField(max_length=1000,blank=True,null=True)




