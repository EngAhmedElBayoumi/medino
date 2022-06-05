from django.contrib import admin
from .models import Post,Comment,Post_ar,Comment_ar

# Register your models here.
admin.site.register(Post)

admin.site.register(Comment)

admin.site.register(Post_ar)

admin.site.register(Comment_ar)
