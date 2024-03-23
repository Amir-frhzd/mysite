from django import template
from blog.models import Post
from django.utils import timezone
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