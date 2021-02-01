from django.shortcuts import render, get_object_or_404


from django.views import generic

from blog.models import BlogAuthor, Blog, Comment

from django.views.generic.edit import CreateView

from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

@login_required
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

    # enable paginating by 5
    paginate_by = 5


class BloggerListView(generic.ListView):
    """View class for listing all bloggers"""
    model = BlogAuthor


class BlogDetailView(generic.DetailView):
    """View class that shows details for a particular blog"""
    model = Blog

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['comment'] = Comment.objects.all()
        return context


class BloggerDetailView(generic.DetailView):
    """View class that shows details for a particular blogger"""
    model = BlogAuthor

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(BloggerDetailView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['blog'] = Blog.objects.all()
        return context


class BlogCommentCreate(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['body']
    success_url = reverse_lazy('blogs_list')

    def form_valid(self, form):
        """
        Add author and associated blog to form data before setting it as valid (so it is saved to model)
        """
        # Add logged-in user as author of comment
        form.instance.author = self.request.user
        # Associate comment with blog based on passed id
        form.instance.blog = get_object_or_404(Blog, pk=self.kwargs['pk'])
        # Call super-class form validation behavior
        return super(BlogCommentCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(BlogCommentCreate, self).get_context_data(**kwargs)
        # Get the blogger object from the "pk" URL parameter and add it to the context
        context['blog'] = get_object_or_404(Blog, pk=self.kwargs['pk'])
        return context


