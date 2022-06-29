from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.exceptions import NotFound
from .permissions import IsOwnerOrReadOnly
from .serializers import (ChannelSerializer, 
                          PostSerializer, 
                          CommentSerializer,
                          DetailedPostSerializer, 
                          DetailedChannelSerializer)
from .models import Post, Channel, Comment

# Create your views here.


class PostListCreateAPIView(generics.ListCreateAPIView):
    """
    List, create view for model Post
    """
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        channel_id = serializer.validated_data.get('channel_id')
        try:
            channel = Channel.objects.get(pk=channel_id)
            files = self.request.FILES.getlist('file',None)
            return serializer.save(owner=self.request.user,channel = channel,context={'files':files})
        except Channel.DoesNotExist:
            raise NotFound(detail='There is no channel with that id')
        

class PostRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, destroy view for model Post
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = DetailedPostSerializer

class ChannelListCreateAPIView(generics.ListCreateAPIView):
    """
    List, create view for model Channel
    """
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer
    
    def perform_create(self, serializer):
        owner = self.request.user
        channel =  serializer.save(owner=owner)
        channel.members.add(owner)
        
class ChannelRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, destroy view for model Channel
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Channel.objects.all()
    serializer_class = DetailedChannelSerializer

class CommentCreateAPIView(generics.CreateAPIView):
    """
    Create view for model Comment
    """
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    def perform_create(self, serializer):
        post_id = serializer.validated_data.get('post_id')
        print(post_id)
        try:
            post = Post.objects.get(pk=post_id)
            return serializer.save(owner=self.request.user,post = post)
        except Post.DoesNotExist:
            raise NotFound(detail='There is no post with that id')
    