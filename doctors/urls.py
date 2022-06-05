from django.urls import path
from doctors import views
app_name='doctors'
urlpatterns = [
    path('doctors',views.doctors,name='doctors'),   
    path('add_doctor',views.add_doctor,name='add_doctor'),


    path('doctors_ar',views.doctors_ar,name='doctors_ar'),   
    path('add_doctor_ar',views.add_doctor_ar,name='add_doctor_ar'),
]
