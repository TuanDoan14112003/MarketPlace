from django.urls import path,include
from . import views
urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
    path('activate/<str:uid>/<str:token>/', views.UserActivationView.as_view()),
    
]
