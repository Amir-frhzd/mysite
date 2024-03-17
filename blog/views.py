from django.shortcuts import render,get_object_or_404
from blog.models import Post
from django.utils import timezone

def blog_view(request):
    
    posts=Post.objects.filter(published_date__lte=timezone.now())
    
    context ={'posts':posts}
    

    return render(request,"blog/blog-home.html",context)

def blog_single(request,pid):
    posts = get_object_or_404(Post,pk=pid)
    posts.counted_view += 1
    posts.save()
    context ={'posts':posts}

 
    return render(request,'blog/blog-single.html',context)

def test(request,pid):
    posts = get_object_or_404(Post,pk=pid)
    context ={'posts':posts}
    return render(request,'test.html',context)


    #your code
# Create your views here.
