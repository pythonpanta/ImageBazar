from django.shortcuts import render
from .models import Category, Post
def Home(request):
    post_obj=Post.objects.all().order_by('?')
    cat=Category.objects.all()
    context={'post_obj':post_obj,'cat':cat}
    return render(request,'app/index.html',context)
def Details(request,id):
    post_obj=Post.objects.filter(category_id=id).order_by('?')
    cat=Category.objects.all()
    context={'post_obj':post_obj,'cat':cat}
    return render(request,'app/index.html',context)