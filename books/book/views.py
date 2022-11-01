from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

from .models import Book, Author


def index(request):
    return HttpResponse("<h2><a href = \"books/\">Книги!!!!!!!</a></h2>")


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'book/author_detail.html'


class AuthorCreateView(CreateView):
    model = Author
    fields = ['name', 'birth_date']


class AuthorUpdateView(UpdateView):
    model = Author
    fields = ['name', 'birth_date']


class AuthorDeleteView(DeleteView):
    model = Author
    success_url = reverse_lazy('book:author_list')


class AuthorListView(ListView):
    model = Author
    template_name = 'book/author_index.html'
    paginate_by = 20

    def get_ordering(self):
        return 'name'


class BookCreateView(CreateView):
    model = Book
    fields = ['title', 'author', 'pub_date', 'image']


class BookUpdateView(UpdateView):
    model = Book
    fields = ['title', 'author', 'pub_date', 'image']


class BookListView(ListView):
    model = Book
    template_name = 'book/index.html'
    paginate_by = 20

    def get_ordering(self):
        return 'title'


class BookDetailView(DetailView):
    model = Book
    template_name = 'book/detail.html'


class BookDeleteView(DeleteView):
    model = Book
    success_url = reverse_lazy('book:book_list')
