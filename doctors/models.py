from django.db import models

# Create your models here.
class doctor(models.Model):
    name = models.CharField(max_length=100)
    Specialization=models.CharField(max_length=1000)
    address = models.CharField(max_length=1000)
    phone=models.CharField(max_length=12)
    image=models.ImageField(upload_to=('static/images'),blank=True)
    create_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['-create_at']

#=================ar=================

class doctor_ar(models.Model):
    name = models.CharField(max_length=100)
    Specialization=models.CharField(max_length=1000)
    address = models.CharField(max_length=1000)
    phone=models.CharField(max_length=12)
    image=models.ImageField(upload_to=('static/images'),blank=True)
    create_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['-create_at']
