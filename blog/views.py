from audioop import reverse
from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from .models import Post
from .form import blog_form,commentform
from .filters import blogfilter
# Create your views here.
def blog (request):
    list_blog = Post.objects.all()
     # filter
    myfilter=blogfilter(request.GET,queryset=list_blog)
    list_blog=myfilter.qs
    # endfilter
    
       # pagination
    paginator = Paginator(list_blog, 8) # Show 8 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
       # end pagination
   
    context = {'blogs':page_obj,'myfilter':myfilter}
    return render(request,'blog_home.html',context)



def blog_details (request , slug):
    post=Post.objects.get(slug=slug)
    
    
    if request.method == 'POST':
        form =commentform(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.create_by = request.user
            comment.post=post
            comment.save()
            form =commentform()
    else:
        form =commentform()

    post=Post.objects.get(slug=slug)
    context = {'blogs':blog_details,'post':post,'form':form}
    return render(request,'blog_details.html',context)



    
def add_blog (request):
    if request.method == 'POST':
        form=blog_form(request.POST,request.FILES)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.create_by = request.user
            myform.save() 
            form=blog_form()
    else:
        form=blog_form()

    return render(request,'add_blog.html',{'form':form})



#========================ar==============================
def blog_ar (request):
    list_blog = Post.objects.all()
     # filter
    myfilter=blogfilter(request.GET,queryset=list_blog)
    list_blog=myfilter.qs
    # endfilter
    
       # pagination
    paginator = Paginator(list_blog, 8) # Show 8 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
       # end pagination
   
    context = {'blogs':page_obj,'myfilter':myfilter}
    return render(request,'blog_home_ar.html',context)



def blog_details_ar (request , slug):
    post=Post.objects.get(slug=slug)
    
    
    if request.method == 'POST':
        form =commentform(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.create_by = request.user
            comment.post=post
            comment.save()
            form =commentform()
    else:
        form =commentform()

    post=Post.objects.get(slug=slug)
    context = {'blogs':blog_details_ar,'post':post,'form':form}
    return render(request,'blog_details_ar.html',context)



    
def add_blog_ar (request):
    if request.method == 'POST':
        form=blog_form(request.POST,request.FILES)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.create_by = request.user
            myform.save() 
            form=blog_form()
    else:
        form=blog_form()

    return render(request,'add_blog_ar.html',{'form':form})



