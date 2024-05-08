from django import template
from blog.models import Post
from django.utils import timezone
from blog.models import Category,Comment
register = template.Library()

@register.simple_tag(name='totalposts')
def function():
    posts=Post.objects.filter(status=1,published_date__lte=timezone.now()).count()
    return posts
@register.filter
def snippet(value,arg=20):
    return value[:arg]

@register.inclusion_tag('blog/blog-popular-posts.html')
def latesposts(arg=3):
    posts = Post.objects.filter(status=1,published_date__lte=timezone.now()).order_by('published_date')[:arg]
    return {'posts':posts}

@register.simple_tag(name='comments_count')
def function(pid):
    return Comment.objects.filter(post=pid,approved=True).count()
@register.inclusion_tag('blog/blog-post-categories.html')
def postcategories():
    posts=Post.objects.filter(status=1,published_date__lte=timezone.now())
    categories=Category.objects.all()
    cat_dic={}
    for name in categories:
        cat_dic[name]=posts.filter(category=name).count()
    return {'categories' : cat_dic}

