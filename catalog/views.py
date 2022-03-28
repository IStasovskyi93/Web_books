from django.shortcuts import render
from django.http import *
from .models import Book, Author, Genre
from django.views import generic, View
from django.urls import reverse


def home(request):
    num_books = Book.objects.all().count()
    num_authors = Author.objects.all().count()
    num_genres = Genre.objects.all().count()
    return render(request, 'catalog/home.html', context={'num_books': num_books, 'num_authors': num_authors,
                                                'num_genres': num_genres},)


class BookListView(generic.ListView):
    model = Book
    paginate_by = 3


class BookDetailView(generic.DetailView):
    model = Book


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 3
