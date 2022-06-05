from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    description=models.CharField(max_length=1000)
    subject = models.TextField()
    image=models.ImageField(upload_to=('static/blog/images'),blank=True)
    create_by=models.ForeignKey(User,related_name='blog_owner',on_delete=models.CASCADE)
    create_at=models.DateTimeField(auto_now=True)
    slug=models.SlugField(blank=True, null=True)
    class Meta:
        ordering = ['-create_at']

    def save(self,*args,**kwargs):
        self.slug= slugify(self.title)
        super(Post,self).save(*args,**kwargs)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post=models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE)
    message=models.TextField(max_length=200)
    create_by=models.ForeignKey(User,related_name='post_owner',on_delete=models.CASCADE)
    create_at=models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-create_at']


#==============================ar========================================

class Post_ar(models.Model):
    title = models.CharField(max_length=100)
    description=models.CharField(max_length=1000)
    subject = models.TextField()
    image=models.ImageField(upload_to=('static/blog/images'),blank=True)
    create_by=models.ForeignKey(User,related_name='blog_ow',on_delete=models.CASCADE)
    create_at=models.DateTimeField(auto_now=True)
    slug=models.SlugField(blank=True, null=True)
    class Meta:
        ordering = ['-create_at']

    def save(self,*args,**kwargs):
        self.slug= slugify(self.title)
        super(Post,self).save(*args,**kwargs)

    def __str__(self):
        return self.title

class Comment_ar(models.Model):
    post=models.ForeignKey(Post,related_name='comments_ar',on_delete=models.CASCADE)
    message=models.TextField(max_length=200)
    create_by=models.ForeignKey(User,related_name='post_ow',on_delete=models.CASCADE)
    create_at=models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-create_at']
   
