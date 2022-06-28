from django.urls import path
from . import views
urlpatterns = [
    path('',views.redocly_view,name='doc')
]