from django.urls import path
from home import views
app_name='home'
urlpatterns = [
    path('home',views.home,name='home'),
    path('about',views.about,name='about'),



    path('home_ar',views.home_ar,name='home_ar'),
    path('about_ar',views.about_ar,name='about_ar'),
    
]