from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout 
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . models import contact
from.forms import imageform

def register(request):
    if request.method=='POST':
        username= request.POST.get('username','')
        email=request.POST.get('email','')
        password=request.POST.get('password','')
        confirm_password=request.POST.get('confirm_password','')

        if not username or not email or not password:
            messages.error(request,'All field are required!.')
        elif password !=confirm_password:
            messages.error(request,'Password do not match')
        elif User.objects.filter(username=username).exists():
            messages.error(request,'Username already exists ')
        elif User.objects.filter(email=email).exists():
            messages.error(request,'Email already exists ')    
        else:
          
          user=User.objects.create_user(username=username, email=email, password=password)
          user.save()
          messages.success(request,'Account created successfully  🎉! please login')
        return redirect('login_view')          
    return render(request,'registerpage.html')

def login_view(request):
    if request.method=='POST':
        username=request.POST.get('username','')
        password=request.POST.get('password','')

        user=authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request,'Invalid username or password ')

    return render(request,'loginpage.html')

def logout_view(request):
    logout(request)
    messages.success(request,'Logged out successfully !.')
    return redirect('login_view')

def live(request):
    return render(request,'livesession.html')

def faq(request):
    return render(request,'faq.html')

def contact_view(request):
    if request.method=="POST":
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        message=request.POST.get('message','')
        if  name and email and message:
            contact.objects.create(name=name, email=email, message=message)
            messages.success(request,"Your message has been sent successfully !.")  
            return redirect('contact_view')  
        else:
            messages.error(request,'Please fill in all fields.  ')

    return render(request,'contact.html')

def index(request):
    return render(request,'index.html')



def celebrityinfo(request):
    return render(request,'celebrityinfo.html')

def home(request):
    return render(request,'home.html',{'user': request.user})


from django.shortcuts import render
from .forms import imageform  # Make sure to import the correct form

from django.shortcuts import render
from django.contrib import messages
from .forms import imageform
from django.contrib import messages

def howitwork(request):
    if request.method == "POST":
        form = imageform(request.POST, request.FILES)
        if form.is_valid():  # Check if the form is valid
            form.save()  # Save the form data
            messages.success(request, 'Photo uploaded successfully! Your celebrity twin will be matched soon.')
        else:
            messages.error(request, 'There was an error with your upload. Please try again.')
    else:
        form = imageform()  # Create an empty form for GET requests
            
    return render(request, 'howitwork.html', {'form': form})


# Create your views here.
