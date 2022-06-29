from django.urls import path
from . import views
urlpatterns = [
    path('posts/',views.PostListCreateAPIView.as_view(),name='post-list-create'),
    path('posts/<int:pk>/',views.PostRetrieveUpdateDestroyAPIView.as_view(),name='post-detail'),
    path('channels/',views.ChannelListCreateAPIView.as_view()),
    path('channels/<int:pk>/',views.ChannelRetrieveUpdateDestroyAPIView.as_view(),name='channel-detail'),
    path('comments/create/',views.CommentCreateAPIView.as_view())
]