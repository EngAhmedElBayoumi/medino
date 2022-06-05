from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.
class illnesses(models.Model):
    illness_name = models.CharField(max_length=100)
    about_illness=models.CharField(max_length=1000)
    protection=models.TextField()
    Symptoms = models.TextField()
    diagnosis = models.TextField()
    image=models.ImageField(upload_to=('static/illnesses/images'),blank=True)
    create_by=models.ForeignKey(User,related_name='illnesses_owner',on_delete=models.CASCADE)
    create_at=models.DateTimeField(auto_now=True)
    slug=models.SlugField(blank=True, null=True)
    class Meta:
        ordering = ['-create_at']

    def save(self,*args,**kwargs):
        self.slug= slugify(self.illness_name)
        super(illnesses,self).save(*args,**kwargs)

    def __str__(self):
        return self.illness_name


#=======================ar===================

class illnesses_ar(models.Model):
    illness_name = models.CharField(max_length=100)
    about_illness=models.CharField(max_length=1000)
    protection=models.TextField()
    Symptoms = models.TextField()
    diagnosis = models.TextField()
    image=models.ImageField(upload_to=('static/illnesses/images'),blank=True)
    create_by=models.ForeignKey(User,related_name='illnesses_ow',on_delete=models.CASCADE)
    create_at=models.DateTimeField(auto_now=True)
    slug=models.SlugField(blank=True, null=True)
    class Meta:
        ordering = ['-create_at']

    def save(self,*args,**kwargs):
        self.slug= slugify(self.illness_name)
        super(illnesses,self).save(*args,**kwargs)

    def __str__(self):
        return self.illness_name