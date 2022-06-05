from django.shortcuts import render
from django.core.paginator import Paginator
from .models import advice as Advice
from .filters import advicefilter

# Create your views here.

def departments (request):
    list_advice = Advice.objects.all()

     # filter
    myfilter=advicefilter(request.GET,queryset=list_advice)
    list_advice=myfilter.qs
    # endfilter

    # pagination
    paginator = Paginator(list_advice, 3) # Show 8 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # end pagination

    context = {'advices':page_obj,'myfilter':myfilter}
    return render(request,'departments.html',context)


def departments_ar (request):
    list_advice = Advice.objects.all()

     # filter
    myfilter=advicefilter(request.GET,queryset=list_advice)
    list_advice=myfilter.qs
    # endfilter

    # pagination
    paginator = Paginator(list_advice, 3) # Show 8 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # end pagination

    context = {'advices':page_obj,'myfilter':myfilter}
    return render(request,'departments_ar.html',context)