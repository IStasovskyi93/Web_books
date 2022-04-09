from django.shortcuts import render
from django.http import *
from .models import Book, Author, Genre
from django.views import generic, View
from django.urls import reverse_lazy
from .forms import AuthorForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView


def home(request):
    num_books = Book.objects.all().count()
    num_authors = Author.objects.all().count()
    num_genres = Genre.objects.all().count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    return render(request, 'catalog/home.html', context={'num_books': num_books, 'num_authors': num_authors,
                                                'num_genres': num_genres, 'num_visits': num_visits})


def addAuthor(request):
    author = Author.objects.all()
    authorsform = AuthorForm()
    return render(request, "catalog/add_author.html", {'form': authorsform, 'author': author})


# create author page
def createAuthor(request):
    if request.method == "POST":
        author = Author()
        author.name = request.POST.get("name")
        author.nationality = request.POST.get("nationality")
        author.date_of_birth = request.POST.get("date_of_birth")
        author.save()
        return HttpResponseRedirect("/add_author/")


# delete author
def delAuthor(request, id):
    try:
        author = Author.objects.get(id=id)
        author.delete()
        return HttpResponseRedirect("/add_author/")
    except Author.DoesNotExist:
        return HttpResponseNotFound("<h2>Authora nie znaleziono</h2>")


# edit author objects
def editAuthor(request, id):
    author = Author.objects.get(id=id)
    if request.method == "POST":
        author.name = request.POST.get("name")
        author.nationality = request.POST.get("nationality")
        author.date_of_birth = request.POST.get("date_of_birth")
        author.date_of_death = request.POST.get("date_of_death")
        author.save()
        return HttpResponseRedirect("/add_author/")
    else:
        return render(request, "catalog/edit_author.html", {"author": author})


class BookCreate(CreateView):
    model = Book
    fields = '__all__'
    success_url = reverse_lazy('books')


class BookUpdate(UpdateView):
    model = Book
    fields = '__all__'
    success_url = reverse_lazy('books')


class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('books')


class BookListView(generic.ListView):
    model = Book
    paginate_by = 3


class BookDetailView(generic.DetailView):
    model = Book


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 3


class AuthorDetailView(generic.DetailView):
    model = Author
