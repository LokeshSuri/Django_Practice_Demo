from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact

def home(request):
    post=Contact.objects.all()
    return render(request,"base.html",{"post":post})
# def demo(request):
#     return HttpResponse("Start the functionality of the Application.....")

# def loki(request):
#     return render(request, 'base.html', {'age':26})
def demo(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        image=request.FILES.get('image')
        
        k=Contact(name=name,email=email,message=message,image=image)
        k.save()
    return render(request, "demo.html")
