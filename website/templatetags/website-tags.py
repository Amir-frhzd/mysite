from django import template
from blog.models import Post
from django.utils import timezone
from blog.models import Category
register = template.Library()

@register.inclusion_tag('website/latestposts.html')
def latestposts(arg=6):
    posts = Post.objects.filter(status=1,published_date__lte=timezone.now()).order_by('published_date')[:arg]
    return {'posts':posts}
@register.filter
def snippet(value,arg=20):
    return value[:arg]
