from django.urls import path
from illnesses import views
app_name='illnesses'
urlpatterns = [
    path('illnesses',views.illness,name='illnesses_home'),
    path('illnesses_details:<str:slug>',views.illnesses_details,name='illnesses_details'),


    path('illnesses_ar',views.illness_ar,name='illnesses_home_ar'),
    path('<str:slug>',views.illnesses_details_ar,name='illnesses_details_ar'),
]