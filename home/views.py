from django.shortcuts import render
from django.core.paginator import Paginator
from doctors.models import doctor as Doctor
from blog.models import Post
from first_aid.models import advice as Advice
#=====================ar============================
from doctors.models import doctor_ar as Doctor_ar
from blog.models import Post_ar
from first_aid.models import advice_ar as Advice_ar
# Create your views here.
def home (request):
    #doctor
    list_doctor = Doctor.objects.all()
    paginator_doctor = Paginator(list_doctor, 4) 
    page_number = request.GET.get('page')
    page_doc = paginator_doctor.get_page(page_number)
    #end
    #blog
    list_blog = Post.objects.all()
    paginator_blog = Paginator(list_blog, 3) # Show 8 contacts per page.
    page_number = request.GET.get('page')
    page_blog = paginator_blog.get_page(page_number)
    #end
    #advice
    list_advice = Advice.objects.all()
    paginator_advice = Paginator(list_advice, 3) # Show 8 contacts per page.
    page_number = request.GET.get('page')
    page_advice  = paginator_advice.get_page(page_number)
    #end


    context = {'doctors':page_doc,'blogs':page_blog,'advices':page_advice}

    return render(request,'index.html',context)


def about (request):
    return render(request,'about.html')




#=====================ar==========================
def home_ar (request):
    #doctor
    list_doctor = Doctor_ar.objects.all()
    paginator_doctor = Paginator(list_doctor, 4) 
    page_number = request.GET.get('page')
    page_doc = paginator_doctor.get_page(page_number)
    #end
    #blog
    list_blog = Post_ar.objects.all()
    paginator_blog = Paginator(list_blog, 3) # Show 8 contacts per page.
    page_number = request.GET.get('page')
    page_blog = paginator_blog.get_page(page_number)
    #end
    #advice
    list_advice = Advice_ar.objects.all()
    paginator_advice = Paginator(list_advice, 3) # Show 8 contacts per page.
    page_number = request.GET.get('page')
    page_advice  = paginator_advice.get_page(page_number)
    #end


    context = {'doctors':page_doc,'blogs':page_blog,'advices':page_advice}

    return render(request,'index_ar.html',context)


def about_ar (request):
    return render(request,'about_ar.html')
    

