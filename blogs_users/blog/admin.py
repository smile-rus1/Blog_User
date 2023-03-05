from django.contrib import admin
from .models import *


class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    list_display_links = ("id", "title")
    search_fields = ("title",)
    # prepopulated_fields = {"slug": ("title",)}


admin.site.register(Post, PostAdmin)
