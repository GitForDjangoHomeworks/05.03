from django.shortcuts import render
from django.views.generic import ListView, UpdateView, DeleteView, CreateView, DetailView
from django.urls import reverse_lazy
from .models import Blog
from .forms import BlogForm
# Create your views here.

class BlogsListView(ListView):
    model = Blog
    context_object_name = 'blogs'
    template_name = 'blogs_view.html'

class BlogDetailView(DetailView):
    model  = Blog
    template_name = 'blogs_detail.html'
    context_object_name = 'blog'
  

class BlogCreateView(CreateView):
    template_name = 'blogs_form.html'
    model = Blog
    success_url = reverse_lazy('blogs:blogs_view')
    form_class = BlogForm

class BlogUpdateView(UpdateView):
    template_name = 'blogs_form.html'
    model = Blog
    success_url = reverse_lazy('blogs:blogs_view')
    form_class = BlogForm

class BlogDeleteView(DeleteView):
    template_name = 'blogs_delete.html'
    model = Blog
    success_url = reverse_lazy('blogs:blogs_view')