from django.urls import path,include

urlpatterns = [
    path('auth/',include('authentication.urls')),
    path('social/',include('social.urls')),
    path('doc/',include('doc.urls'))
] 
