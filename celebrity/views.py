from django.shortcuts import render

def register(request):
    return render(request,'registerpage.html')

def login(request):
    return render(request,'loginpage.html')

def live(request):
    return render(request,'livesession.html')

def faq(request):
    return render(request,'faq.html')

def contact(request):
    return render(request,'contact.html')

def index(request):
    return render(request,'index.html')

def howitwork(request):
    return render(request,'howitwork.html')

def celebrityinfo(request):
    return render(request,'celebrityinfo.html')




# Create your views here.
