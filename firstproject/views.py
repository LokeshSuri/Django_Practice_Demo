from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello This is my First Project!!!")
def demo(request):
    return HttpResponse("Let's get started our learning....")