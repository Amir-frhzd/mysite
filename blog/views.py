from django.shortcuts import render,get_object_or_404
from blog.models import Post,Comment
from django.utils import timezone
from blog.forms import CommentForm
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
def blog_view(request,cat_name=None,tag_name=None):
    
    posts=Post.objects.filter(published_date__lte=timezone.now(),status=1)
    if cat_name:
        posts=posts.filter(category__name=cat_name)
    if tag_name:
        posts=posts.filter(tags__name__in=[tag_name])
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
    if request.method == 'POST':
        form =CommentForm(request.POST)
        
        if form.is_valid():
            
            form.save()
            messages.add_message(request,messages.SUCCESS,"Your comment submited sucssesfully")
        else :
            messages.add_message(request,messages.ERROR,"Your comment  didnt submited sucssesfully")
    
    posts = get_object_or_404(Post,pk=pid,status=1,published_date__lte=timezone.now())
    all_post=Post.objects.filter(status=1,published_date__lte=timezone.now())
    next_post =all_post.filter(id__gt=pid).order_by('id').first()
    previous_post=all_post.filter(id__lt=pid).order_by('-id').first()
    posts.counted_view += 1
    posts.save()
    if not posts.login_require :
        comments = Comment.objects.filter(post=posts.id,approved=True)
        form = CommentForm()
        context ={'posts':posts,'next_post':next_post,'previous_post':previous_post,'comments':comments,'form':form}
        return render(request,'blog/blog-single.html',context)
    elif request.user.is_authenticated :
        comments = Comment.objects.filter(post=posts.id,approved=True)
        form = CommentForm()
        context ={'posts':posts,'next_post':next_post,'previous_post':previous_post,'comments':comments,'form':form}
        return render(request,'blog/blog-single.html',context)
    else :
        return HttpResponseRedirect(reverse('accounts:login'))


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
