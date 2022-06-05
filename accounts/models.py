from cProfile import Profile
from cmath import phase
from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.




class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    address=models.CharField(max_length=50)
    phone=models.CharField(max_length=15)
    image=models.ImageField(upload_to='static/profileimage')
    about_me=models.CharField(max_length=1000)
    jop_title=models.CharField(max_length=50)



@receiver(post_save, sender=User)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
