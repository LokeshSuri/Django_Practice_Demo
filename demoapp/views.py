from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("This is my First APP!!!")

def demo(request):
    return HttpResponse("Start the functionality of the Application.....")
def loki(request):
    return render(request, 'base.html')