from django.shortcuts import render

# Create your views here.
from django.views import generic

from blog.models import BlogAuthor, Blog, Comment
from django.views.generic import ListView, DetailView


def index(request):
    """View function for Home page site"""
    # Generate counts of some of the main objects
    num_bloggers = BlogAuthor.objects.count()
    num_blogs = Blog.objects.count()
    num_comments = Comment.objects.count()
    context = {
        'num_bloggers': num_bloggers,
        'num_blogs': num_blogs,
        'num_comments': num_comments,
    }
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context)


class BlogListView(generic.ListView):
    """View class for listing all blog post"""
    model = Blog
