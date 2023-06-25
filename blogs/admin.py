from django.contrib import admin
from .models import Blog
# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title']
    list_display_links = ['pk',]
admin.site.register(Blog,BlogAdmin)