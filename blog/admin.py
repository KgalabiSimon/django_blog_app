from django.contrib import admin

from blog.models import BlogAuthor, Category, Blog, Comment

# Register your models here.

admin.site.register(BlogAuthor)
admin.site.register(Category)
admin.site.register(Blog)
admin.site.register(Comment)