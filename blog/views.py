from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from blog.models import Post
from django.core.urlresolvers import reverse_lazy


class PostLV(ListView):
	model = Post


class PostDV(DetailView):
	model = Post


class PostCV(CreateView):
	model = Post
	fields = ['title', 'image', 'description']
	success_url = reverse_lazy('blog_index')


class PostUV(UpdateView):
	model = Post
	fields = ['title', 'image', 'description']
	success_url = reverse_lazy('blog_index')


class PostRV(DeleteView):
	model = Post
	success_url = reverse_lazy('blog_index')
