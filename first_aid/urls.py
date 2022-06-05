from django.urls import path
from . import views
app_name='departments'
urlpatterns = [
    path('departments',views.departments,name='departments'),

    path('departments_ar',views.departments_ar,name='departments_ar'),
]