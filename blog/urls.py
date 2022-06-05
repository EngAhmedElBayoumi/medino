from django.urls import path
from blog import views
app_name='blog'
urlpatterns = [
    path('blog',views.blog,name='blog_home'),
    path('add_blog',views.add_blog,name='add_blog'),
    path('blog_details:<str:slug>',views.blog_details,name='blog_details'),



     path('blog_ar',views.blog_ar,name='blog_home_ar'),
    path('add_blog_ar',views.add_blog_ar,name='add_blog_ar'),
    path('<str:slug>',views.blog_details_ar,name='blog_details_ar'),

]