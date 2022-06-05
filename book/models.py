from django.db import models

# Create your models here.
class book(models.Model):
    name=models.CharField(max_length=30)
    image=models.ImageField(upload_to=('static/books'),blank=True)
    book=models.FileField(upload_to=('static/books'))
    create_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['-create_at']


#===================ar======================

class book_ar(models.Model):
    name=models.CharField(max_length=30)
    image=models.ImageField(upload_to=('static/books'),blank=True)
    book=models.FileField(upload_to=('static/books'))
    create_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['-create_at']