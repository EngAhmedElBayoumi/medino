from email.message import Message
from django.contrib import messages
from django.conf import settings
from django.shortcuts import render
from .models import Info
from django.core.mail import send_mail

# Create your views here.
def contact (request):
    myinfo=Info.objects.last()

    if request.method=='POST':
        subject=request.POST['subject']
        email=request.POST['email']
        message=request.POST['message']

        send_mail(
           subject,
            message,
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False
        )
        messages.success(request,'MAIL SEND')

    return render(request,'contact.html',{'myinfo':myinfo})



def contact_ar (request):
    myinfo=Info.objects.last()

    if request.method=='POST':
        subject=request.POST['subject']
        email=request.POST['email']
        message=request.POST['message']

        send_mail(
           subject,
            message,
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False
        )
        messages.success(request,'MAIL SEND')

    return render(request,'contact_ar.html',{'myinfo':myinfo})