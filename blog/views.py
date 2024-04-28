from django.shortcuts import render,get_object_or_404
from blog.models import Post
from django.utils import timezone
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

def blog_view(request,cat_name=None):
    
    posts=Post.objects.filter(published_date__lte=timezone.now(),status=1)
    if cat_name:
        posts=posts.filter(category__name=cat_name)
    try:
        posts=Paginator(posts,3)
        page_number=request.GET.get('page')
        posts= posts.get_page(page_number)
    except PageNotAnInteger:
        posts=posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)

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
    if request.method == 'POST':
        print("post")
    elif request.method == "GET" :
        print('get')
    
    return render(request,'test.html')

def blog_search(request):
    posts=Post.objects.filter(published_date__lte=timezone.now(),status=1)
    if request.method == 'GET' :
        #print(request.GET.get('s'))
        if s :=request.GET.get('s'):
            posts = posts.filter(content__contains=s)
    context ={'posts':posts}
    return render(request,"blog/blog-home.html",context)



    #your code
# Create your views here.
