from imp import source_from_cache
from .models import Post,Channel, Comment, File
from rest_framework import serializers
from authentication.serializers import CustomUserSerializer



class DetailedChannelSerializer(serializers.ModelSerializer):
    owner = CustomUserSerializer(read_only = True)
    members = CustomUserSerializer(read_only=True,many=True)
    class Meta:
        model = Channel
        fields = '__all__'

class ChannelSerializer(serializers.ModelSerializer):
    
    owner = CustomUserSerializer(read_only = True)
    path = serializers.CharField(source='get_absolute_url')
    class Meta:
        model = Channel
        exclude = ['members']

class CommentSerializer(serializers.ModelSerializer):
    owner = CustomUserSerializer(read_only = True)
    post_id = serializers.IntegerField()
    score = serializers.IntegerField(read_only= True)
    body = serializers.CharField()
    class Meta:
        model = Comment
        exclude = ['post']

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['post_id','file']
        read_only_fields = ['post_id']

class DetailedPostSerializer(serializers.ModelSerializer):
    owner = CustomUserSerializer(read_only = True)
    score = serializers.IntegerField(read_only= True)
    channel_id = serializers.IntegerField()
    comments = CommentSerializer(source='comment_set',many=True,read_only=True)
    file = FileSerializer(source='file_set',many=True,required=False)
    class Meta:
        model = Post
        exclude = ['channel']



class PostSerializer(serializers.ModelSerializer):
    owner = CustomUserSerializer(read_only = True)
    score = serializers.IntegerField(read_only= True)
    channel_id = serializers.IntegerField()
    path = serializers.CharField(source='get_absolute_url',read_only=True)
    file = FileSerializer(source='file_set',many=True,allow_null=True,required=False)
    class Meta:
        model = Post
        exclude = ['channel']

    def save(self,context={},*args,**kwargs):
        post = super().save(*args,**kwargs)
        files = context.get('files',None)
        print(files)
        for file in files:
            File.objects.create(post=post,file=file)
        return post



