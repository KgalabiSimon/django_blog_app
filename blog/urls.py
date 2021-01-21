from django import views
from django.urls import path
from . import views
from blog.views import BlogListView


urlpatterns = [
    path('', views.index, name='index'),
    path('all/', BlogListView.as_view(), name='blogs_list'),
]