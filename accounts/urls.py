from django.urls import path
from . import views
app_name='account'
urlpatterns = [
    path('logout/',views.logout_user,name="logout"),
    path('login',views.login_in,name='login'),
    path('signin',views.registration,name='signin'),
    path('profile',views.profile1,name='profile'),
    path('reset_password',views.resets_password,name='reset_password'),
    path('update_profile',views.update_profile,name='update_profile'),
    path('changepass/<str:id>/',views.changepassword,name='resetpassword2'), 
    #==========================ar==========================
    path('logout_ar/',views.logout_user_ar,name="logout_ar"),
    path('login_ar',views.login_in_ar,name='login_ar'),
    path('signin_ar',views.registration_ar,name='signin_ar'),
    path('profile_ar',views.profile1_ar,name='profile_ar'),
    path('reset_password_ar',views.resets_password_ar,name='reset_password_ar'),
    path('update_profile_ar',views.update_profile_ar,name='update_profile_ar'),
    path('changepass_ar/<str:id>/',views.changepassword_ar,name='resetpassword2_ar'), 
   
]