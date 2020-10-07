from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from bookmark.models import Bookmark
from django.core.urlresolvers import reverse_lazy


class BookmarkLV(ListView):
	model = Bookmark


class BookmarkDV(DetailView):
	model = Bookmark


class BookmarkCV(CreateView):
	model = Bookmark
	fields = ['title', 'url']
	success_url = reverse_lazy('bookmark_index')


class BookmarkUV(UpdateView):
	model = Bookmark
	fields = ['title', 'url']
	success_url = reverse_lazy('bookmark_index')


class BookmarkRV(DeleteView):
	model = Bookmark
	success_url = reverse_lazy('bookmark_index')
