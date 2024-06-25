from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog

def home(request):
    post=Blog.objects.all()
    return render(request, "home.html", {"post":post})
# def demo(request):
#     return HttpResponse("Start the functionality of the Application.....")

def loki(request):
    return render(request, 'base.html', {'age':26})
def gani(request):
    return render(request, 'demo.html',{'name': "Lokesh Suri"})
