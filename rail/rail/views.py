from django.shortcuts import render,redirect,HttpResponse
from api.emailbackend import emailbackend
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.decorators import login_required

from api.models import CustomUser
from api.models import *


from django.contrib.auth.decorators import login_required

from django.contrib import messages
def base(request):
    return render(request,'base.html') 
@login_required(login_url='/')

def home(request):
    return render(request,'home.html')
def loginn(request):
    return render(request,'login.html')

def dologin(request):
    
    if request.method == "POST":
       user = emailbackend.authenticate(request,
                                        username=request.POST.get('email'),
                                        password=request.POST.get('password'),)
       if user!=None:
           login(request,user)
           user_type = user.user_type
           if user_type == '1':
               return redirect('home')
          
           else:
               messages.error(request,'Email and Password Are Invalid !')
               return redirect('loginn')
       else:
           messages.error(request,'Email and Password Are Invalid !')
           return redirect('loginn')
       
       
def dologout(request):
    logout(request)
    return redirect('loginn')

@login_required(login_url='/')
def view(request):
    return render(request,'view.html')



def profile(request):
    user=CustomUser.objects.get(id=request.user.id)
    dict={
        'user':user,
    }
    
    return render(request,'profile.html')
@login_required(login_url='/')

def profileUpdate(request):
    if request.method=='POST':
        profile_pic=request.FILES.get('profile_pic')
        first_name=request.POST.get('firstname')
        last_name=request.POST.get('lastname')
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get ('password')
        gender=request.POST.get ('gender')
        address=request.POST.get ('address')
        dob=request.POST.get ('dob')

        
        
        
        try:
            user=CustomUser.objects.get(id=request.user.id)
            user.first_name=first_name
            user.last_name=last_name
            
            
            if password!=None and password!="":
                user.set_password(password)
            if profile_pic !=None and profile_pic != "":
                user.profile_pic = profile_pic
            
           
            user.save()   
            messages.success(request,"Updated successfully")
            return redirect('profile')
        except:
            messages.error(request,'error occured')
            
            
    return render(request,'profile.html')
def register(request):
    if request.method=="POST":
        profile_pic=request.FILES.get('profile_pic')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get('password')
        mobile=request.POST.get('mobile')
        dob=request.POST.get('dob')
        address=request.POST.get('address')
        gender=request.POST.get('gender')
        
        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request,"Email Already exists")
            return redirect('register')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request,'Username already exists')
            return redirect('register')
        if Client.objects.filter(mobile=mobile).exists():
            messages.warning(request,'Mobile Number already exists')
            return redirect('register')
        
        else:
            user = CustomUser(
                first_name = first_name,
                last_name = last_name,
                username = username,
                email = email,
                profile_pic = profile_pic,
                user_type = 1
            )
        user.set_password(password)
        user.save()   
        client=Client(
                admin=user,
                mobile=mobile,
                gender=gender,
                address=address,
                dob=dob,
                )          
        client.save()
        messages.success(request,'Registered Succesffully')
        return redirect('home')
    
    return render(request,'register.html')