from django.contrib import admin
from .models import Blog

class BlogAdmin(admin.ModelAdmin):
    list_display = ["id","title", "content", "date"]
    fields = ["title", "content"]

admin.site.register(Blog, BlogAdmin)