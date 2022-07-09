from django.contrib.auth import get_user_model
from django.db import models
from PIL import Image
from social.helpers import get_filename
User = get_user_model()
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=get_filename,default='default_avatar.png')
    cover = models.ImageField(upload_to=get_filename,default='default_cover.jpg')
    description = models.TextField(blank=True,null=True)

    @property
    def root_folder(self):
        return 'user_images/'

    def compress(self,path,name,quality=60):
        if not name in ['default_avatar.png','default_cover.jpg']:
            print(f'compressing image')
            image = Image.open(path)
            image.save(path,quality=quality,optimize=True)
        else:
            print("Not compressing image because it is a default image")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        avatar_path = self.avatar.path
        cover_path = self.cover.path
        self.compress(avatar_path,self.avatar.name)
        self.compress(cover_path,self.cover.name)

    def __str__(self):
        return 'Profile for ' + self.user.username