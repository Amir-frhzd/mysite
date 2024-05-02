from django.contrib.sitemaps import Sitemap
from blog.models import Post
from django.utils import timezone


class BlogSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.5

    def items(self):
        return Post.objects.filter(status=1,published_date__lte=timezone.now())

    def lastmod(self, obj):
        return obj.published_date