from django.shortcuts import render
from django.views.generic import ListView, DetailView

from blogs.models import Blog

# Create your views here.
class BlogListView(ListView):
    model = Blog
    template_name = 'blogs/index.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(BlogListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['blogs'] = self.get_queryset()
        return context

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blogs/detail.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        print(self.request)
        context['blog'] = self.get_object()
        return context