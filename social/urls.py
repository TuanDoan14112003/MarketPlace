from django.urls import path
from . import views
urlpatterns = [
    path('posts/',views.PostListCreateAPIView.as_view(),name='post-list-create'),
    path('posts/<int:pk>/',views.PostRetrieveUpdateAPIView.as_view(),name='post-retrieve-update')
]