from django.db import models

# Create your models here.


class advice(models.Model):
    image=models.ImageField(upload_to=('static/advice'))
    title=models.CharField(max_length=400)
    description=models.TextField()
    create_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-create_at']

#=================ar====================

class advice_ar(models.Model):
    image=models.ImageField(upload_to=('static/advice'))
    title=models.CharField(max_length=400)
    description=models.TextField()
    create_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-create_at']