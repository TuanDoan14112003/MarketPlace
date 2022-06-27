from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
import requests
# Create your views here.

class UserActivationView(generics.GenericAPIView):
    def get (self, request, uid, token):
        protocol = 'https://' if request.is_secure() else 'http://'
        web_url = protocol + request.get_host()
        post_url = web_url + "/auth/users/activation/"
        post_data = {'uid': uid, 'token': token}
        response = requests.post(post_url, data = post_data)
        
        status = response.status_code

        if status == 204:
            return Response({'detail':"Your account has been activated"},status=status)
        elif status == 400:
            return Response({'detail':"Invalid activation link"},status=status)
        elif status == 403:
            return Response({'detail':"This activation link has already been used"},status=status)
        else:
            content = response.json()
            return Response(content,status=status)