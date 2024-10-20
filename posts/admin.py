from django.contrib import admin

from posts.models import Post


# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'rate', 'created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at']