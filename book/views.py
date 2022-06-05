from django.shortcuts import render

from django.core.paginator import Paginator
from .models import book as Book
from .filters import bookfilter

# Create your views here.
def books (request):
    list_book = Book.objects.all()
     # filter
    myfilter=bookfilter(request.GET,queryset=list_book)
    list_book=myfilter.qs
    # endfilter
    # pagination
    paginator = Paginator(list_book, 8) # Show 8 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # end pagination
    context = {'books':page_obj,'myfilter':myfilter}
    return render(request,'book.html',context)





def books_ar (request):
    list_book = Book.objects.all()
    # filter
    myfilter=bookfilter(request.GET,queryset=list_book)
    list_book=myfilter.qs
    # endfilter
    # pagination
    paginator = Paginator(list_book, 8) # Show 8 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # end pagination
    context = {'books':page_obj,'myfilter':myfilter}
    return render(request,'book_ar.html',context)