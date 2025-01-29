from django.shortcuts import render,get_object_or_404
from django.http import Http404
from .models import Blog

# Create your views here.

def bloglistview(request):
    blogs = Blog.objects.all()
    context = {
        'blogs':blogs
    }
    return render(request,'blogs.html',context)

def blogdetailview(request,id):
    blog = get_object_or_404(Blog,id=id)
    context = {
        'blog':blog
    }
    return render(request,'blog_detail.html',context=context)
