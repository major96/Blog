from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.views.generic import CreateView, DetailView, ListView, DeleteView, UpdateView
# Create your views here.

class CreatePostView(CreateView):
    template_name = 'create.html'
    model = Post
    form_class = PostForm
    context_object_name = 'form'
    success_url = '/'

class PostListView(ListView):
    template_name = 'list.html'
    model = Post
    ordering = '-pub_date'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    template_name = 'detail.html'
    model = Post
    context_object_name = 'post'

class PostUpdateView(UpdateView):
    template_name = 'create.html'
    model = Post
    form_class = PostForm
    context_object_name = 'form'
    success_url = '/'

class PostDeleteView(DeleteView):
    template_name = 'delete.html'
    model = Post
    context_object_name = 'form'
    success_url ='/'

