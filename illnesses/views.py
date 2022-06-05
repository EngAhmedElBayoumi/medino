from audioop import reverse
from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from .models import illnesses
from .filters import illfilter
# Create your views here.
def illness (request):
   list_ill = illnesses.objects.all()
   
   # filter
   myfilter=illfilter(request.GET,queryset=list_ill)
   list_ill=myfilter.qs
    # endfilter
       # pagination
   paginator = Paginator(list_ill, 4) # Show 8 contacts per page.
   page_number = request.GET.get('page')
   page_obj = paginator.get_page(page_number)
       # end pagination
   context = {'illnesses':page_obj,'myfilter':myfilter}
   return render(request,'illnesses_home.html',context)



def illnesses_details (request , slug):
    post=illnesses.objects.get(slug=slug)
    
    context = {'illnesses':illnesses_details,'post':post,}
    return render(request,'illnesses_details.html',context)


#==============ar============================

def illness_ar (request):
   list_ill = illnesses.objects.all()
   
   # filter
   myfilter=illfilter(request.GET,queryset=list_ill)
   list_ill=myfilter.qs
    # endfilter
       # pagination
   paginator = Paginator(list_ill, 4) # Show 8 contacts per page.
   page_number = request.GET.get('page')
   page_obj = paginator.get_page(page_number)
       # end pagination
   context = {'illnesses':page_obj,'myfilter':myfilter}
   return render(request,'illnesses_home_ar.html',context)



def illnesses_details_ar (request , slug):
    post=illnesses.objects.get(slug=slug)

    context = {'illnesses':illnesses_details_ar,'post':post,}
    return render(request,'illnesses_details_ar.html',context)



