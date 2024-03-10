from django.db import models


class Post(models.Model):
    # iamge =
    # author =
    title = models.CharField(max_length=255)
    content = models.TextField()
    # tags =
    # category =
    counted_view = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return ("%s-%s"%(self.title,self.id))
    class Meta:
        ordering = ['-created_date']

# Create your models here.
