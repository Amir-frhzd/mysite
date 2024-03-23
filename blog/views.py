from django.shortcuts import render,get_object_or_404
from blog.models import Post
from django.utils import timezone

def blog_view(request):
    
    posts=Post.objects.filter(published_date__lte=timezone.now(),status=1)
    
    context ={'posts':posts}
    

    return render(request,"blog/blog-home.html",context)

def blog_single(request,pid):
    posts = get_object_or_404(Post,pk=pid,status=1,published_date__lte=timezone.now())
    all_post=Post.objects.filter(status=1,published_date__lte=timezone.now())
    next_post =all_post.filter(id__gt=pid).order_by('id').first()
    previous_post=all_post.filter(id__lt=pid).order_by('-id').first()
    posts.counted_view += 1
    posts.save()
    context ={'posts':posts,'next_post':next_post,'previous_post':previous_post}

 
    return render(request,'blog/blog-single.html',context)

def test(request):
    #posts = get_object_or_404(Post,pk=pid)
    #context ={'posts':posts}
    return render(request,'test.html')


    #your code
# Create your views here.
