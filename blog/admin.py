from django.contrib import admin
from blog.models import Post,Category
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
class PostAdmin(SummernoteModelAdmin):

    date_hierarchy = "created_date"
    empty_value_display = "-empty-"
    list_display = ["title","author","counted_view","status","published_date"]
    #ordering = ["-created_date"]
    search_fields = ["title","content"]
    list_filter = ('status',)
    summernote_fields = ('content',)

admin.site.register(Category)
admin.site.register(Post,PostAdmin)
