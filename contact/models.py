from pyexpat import model
from django.db import models

# Create your models here.
class Info(models.Model):
    place=models.CharField(max_length=50)
    phone=models.CharField(max_length=20)
    email=models.EmailField(max_length=250)

    class Meta:
        verbose_name=("Info")
        verbose_name_plural=("Info")

    def __str__(self):
        return self.email


#=================ar===============
class Info_ar(models.Model):
    place=models.CharField(max_length=50)
    phone=models.CharField(max_length=20)
    email=models.EmailField(max_length=250)

    class Meta:
        verbose_name=("Info")
        verbose_name_plural=("Info")

    def __str__(self):
        return self.email
