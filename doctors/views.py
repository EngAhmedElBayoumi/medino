from django.shortcuts import render
from .form import doctor_form
from django.core.paginator import Paginator
from .models import doctor as Doctor
from .filters import  doctorfilter

# Create your views here.
def doctors (request):
    list_doctor = Doctor.objects.all()
    
    # filter
    myfilter=doctorfilter(request.GET,queryset=list_doctor)
    list_doctor=myfilter.qs
    # endfilter

    # pagination
    paginator = Paginator(list_doctor, 4) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # end pagination

    context = {'doctors':page_obj,'myfilter':myfilter}
    return render(request,'doctors.html',context)





def add_doctor (request):
    if request.method == 'POST':
        form=doctor_form(request.POST,request.FILES)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.create_by = request.user
            myform.save() 
            form=doctor_form()
    else:
        form=doctor_form()

    return render(request,'add_doctor.html',{'form':form})



#=============================ar============================

def doctors_ar (request):
    list_doctor = Doctor.objects.all()
    
    # filter
    myfilter=doctorfilter(request.GET,queryset=list_doctor)
    list_doctor=myfilter.qs
    # endfilter

    # pagination
    paginator = Paginator(list_doctor, 4) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # end pagination

    context = {'doctors':page_obj,'myfilter':myfilter}
    return render(request,'doctors_ar.html',context)





def add_doctor_ar (request):
    if request.method == 'POST':
        form=doctor_form(request.POST,request.FILES)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.create_by = request.user
            myform.save() 
            form=doctor_form()
    else:
        form=doctor_form()

    return render(request,'add_doctor_ar.html',{'form':form})