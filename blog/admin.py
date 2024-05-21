from django.contrib import admin
from blog.models import Post,Category,Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
class PostAdmin(SummernoteModelAdmin):

    date_hierarchy = "created_date"
    empty_value_display = "-empty-"
    list_display = ["title","author","counted_view","status",'login_require',"published_date"]
    #ordering = ["-created_date"]
    search_fields = ["title","content"]
    list_filter = ('status',)
    summernote_fields = ('content',)
class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = "created_date"
    empty_value_display = "-empty-"
    list_display = ["name","post",'approved',"created_date"]
    #ordering = ["-created_date"]
    search_fields = ["name","post"]
    


admin.site.register(Comment,CommentAdmin)
admin.site.register(Category)
admin.site.register(Post,PostAdmin)
