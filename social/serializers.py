from dataclasses import fields
from .models import Post
from rest_framework import serializers
from authentication.serializers import CustomUserSerializer


class PostSerializer(serializers.ModelSerializer):
    author = CustomUserSerializer(read_only = True)
    score = serializers.IntegerField(read_only= True)
    class Meta:
        model = Post
        fields = '__all__'
