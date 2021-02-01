from django import views
from django.urls import path
from . import views
from blog.views import BlogListView, BloggerListView, BlogDetailView,BloggerDetailView, BlogCommentCreate


urlpatterns = [
    path('', views.index, name='index'),
    path('all/', BlogListView.as_view(), name='blogs_list'),
    path('bloggers/', BloggerListView.as_view(), name='blogger_list'),
    path('<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('bloggers/<int:pk>/', BloggerDetailView.as_view(), name='blogger_detail'),
    path('<int:pk>/create/', BlogCommentCreate.as_view(), name='comment-create')
]