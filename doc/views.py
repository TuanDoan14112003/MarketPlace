from django.shortcuts import render


# Create your views here.

def redocly_view(request):
    return render(request,'doc.html')
