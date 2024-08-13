from django.contrib import admin
from .models import BlogPost, Tag

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_published')
    search_fields = ('title', 'content')

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Tag)
