from tkinter import S
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login ,logout
from .forms import LoginForm, ProfileForm, UserForm
from django.contrib import messages
from .models import Profile
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def login_in(request):
    if request.method =='POST':
        form=LoginForm()
        username = request.POST['username']
        password = request.POST['password']
        user= authenticate(request, username=username , password=password)
        if user is not None:
            login(request, user)
            return redirect('account:profile')
        else:
           messages.warning(request,'هناك خطافى اسم المستخدم او كلمه المرور')
    else:
        form=LoginForm()
    return render(request, 'login.html',{
        'form': form,
    })

def logout_user(request):
    logout(request)
    return render(request,'login.html',{
        'title':'تسجيل الخروج'
    })





def registration(request):
   
    if request.method =="POST":
      first_name = request.POST['first_name']
      last_name = request.POST['last_name']
      username = request.POST['username']
      password1 = request.POST['password1']
      password2 = request.POST['password2']
      email = request.POST['email']
    
      if password1== password2:
        myuser= User.objects.create_user(username,email,password1)
        myuser.first_name=first_name
        myuser.last_name=last_name
        myuser.save()
        return redirect('account:login')
           
      else:
           
           messages.error(request,'كلمه المرور غير متطابقه  ')
           return redirect('account:signin')
    else:  
     return render(request, 'sign-up.html')







def update_profile(request):
    profile=Profile.objects.get(user=request.user)
    if request.method=='POST':
        userform=UserForm(request.POST,instance=request.user)
        profileform=ProfileForm(request.POST,request.FILES,instance=profile)
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            myprofile=profileform.save(commit=False)
            myprofile.user=request.user
            myprofile.save()
            return redirect('account:profile')
    else:
        userform=UserForm(instance=request.user)
        profileform=ProfileForm(instance= profile)
    

    return render(request,'update_profile.html',{'profile':profile,'userform':userform,'profileform':profileform})




def resets_password(request):
    if request.method=="POST":
      username=request.POST["username"]
      user=User.objects.get(username=username)
      profile=Profile.objects.get(user=user)
      user_email=profile
      mail_message= f'hey your Reset password link is http://127.0.0.1:8000/changepass/{user_email}/'
      send_mail('password Reset Request',mail_message,settings.EMAIL_HOST_USER,[user.email],fail_silently=False)
      messages.success(request,'MAIL SEND')
    #   print(mail_message)
   
    return render(request,'reset_password.html')





def profile1(request):
    profile=Profile.objects.get(user=request.user)
    return render(request,'profile.html',{'profile':profile})
    



def changepassword(request,id):
    if request.method=="POST":
    #  username=request.POST["password1"]
    #  user=User.objects.get(username=username)
      password1=request.POST['password1']
    #   password2=request.POST['password2']
      profile=Profile.objects.get(username=id).user
      user=User.objects.get(username=profile)
      user.set_password(password1)
      user.save()
      messages.success(request,'success ')
    #  Profile=profile.objects.get(password1)
      return render(request,'resetpassword2.html')
    return render(request,'resetpassword2.html')


#========================ar===============================

def login_in_ar(request):
    if request.method =='POST':
        form=LoginForm()
        username = request.POST['username']
        password = request.POST['password']
        user= authenticate(request, username=username , password=password)
        if user is not None:
            login(request, user)
            return redirect('account:profile_ar')
        else:
           messages.warning(request,'هناك خطافى اسم المستخدم او كلمه المرور')
    else:
        form=LoginForm()
    return render(request, 'login_ar.html',{
        'form': form,
    })

def logout_user_ar(request):
    logout(request)
    return render(request,'login_ar.html',{
        'title':'تسجيل الخروج'
    })





def registration_ar(request):
   
    if request.method =="POST":
      first_name = request.POST['first_name']
      last_name = request.POST['last_name']
      username = request.POST['username']
      password1 = request.POST['password1']
      password2 = request.POST['password2']
      email = request.POST['email']
    
      if password1== password2:
        myuser= User.objects.create_user(username,email,password1)
        myuser.first_name=first_name
        myuser.last_name=last_name
        myuser.save()
        return redirect('account:login_ar')
           
      else:
           
           messages.error(request,'كلمه المرور غير متطابقه  ')
           return redirect('account:signin_ar')
    else:  
     return render(request, 'sign-up_ar.html')







def update_profile_ar(request):
    profile=Profile.objects.get(user=request.user)
    if request.method=='POST':
        userform=UserForm(request.POST,instance=request.user)
        profileform=ProfileForm(request.POST,request.FILES,instance=profile)
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            myprofile=profileform.save(commit=False)
            myprofile.user=request.user
            myprofile.save()
            return redirect('account:profile_ar')
    else:
        userform=UserForm(instance=request.user)
        profileform=ProfileForm(instance= profile)
    

    return render(request,'update_profile_ar.html',{'profile':profile,'userform':userform,'profileform':profileform})




def resets_password_ar(request):
    if request.method=="POST":
      username=request.POST["username"]
      user=User.objects.get(username=username)
      profile=Profile.objects.get(user=user)
      user_email=profile
      mail_message= f'hey your Reset password link is http://127.0.0.1:8000/changepass/{user_email}/'
      send_mail('password Reset Request',mail_message,settings.EMAIL_HOST_USER,[user.email],fail_silently=False)
      messages.success(request,'MAIL SEND')
    #   print(mail_message)
   
    return render(request,'reset_password_ar.html')





def profile1_ar(request):
    profile=Profile.objects.get(user=request.user)
    return render(request,'profile_ar.html',{'profile':profile})
    

def changepassword_ar(request,id):
    if request.method=="POST":
    #  username=request.POST["password1"]
    #  user=User.objects.get(username=username)
      password1=request.POST['password1']
    #   password2=request.POST['password2']
      profile=Profile.objects.get(username=id).user
      user=User.objects.get(username=profile)
      user.set_password(password1)
      user.save()
      messages.success(request,'success ')
    #  Profile=profile.objects.get(password1)
      return render(request,'resetpassword2_ar.html')
    return render(request,'resetpassword2_ar.html')
