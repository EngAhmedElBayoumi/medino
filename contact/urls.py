from django.urls import path
from contact import views
app_name='contact'
urlpatterns = [
    path('contact',views.contact,name='contact'),
    path('contact_ar',views.contact_ar,name='contact_ar'),
]