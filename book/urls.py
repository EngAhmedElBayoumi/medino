from django.urls import path
from book import views
app_name='book'
urlpatterns = [
    path('book',views.books,name='book'),
    path('book_ar',views.books_ar,name='book_ar'),
]