from django.contrib import admin
from blog.models import Post,Category

# Register your models here.
class PostAdmin(admin.ModelAdmin):

    date_hierarchy = "created_date"
    empty_value_display = "-empty-"
    list_display = ["title","author","counted_view","status","published_date"]
    #ordering = ["-created_date"]
    search_fields = ["title","content"]
    list_filter = ('status',)

admin.site.register(Category)
admin.site.register(Post,PostAdmin)
