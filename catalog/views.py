from django.shortcuts import render
from django.http import *
from .models import Book, Author, Genre
from django.views import generic
from django.urls import reverse_lazy
from .forms import AuthorForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView


def home(request):
    """strona główna z pokazem zagalnej ilości książek, autorów oraz vizytów zalogowanego uzytkownika"""
    num_books = Book.objects.all().count()
    num_authors = Author.objects.all().count()
    num_genres = Genre.objects.all().count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    return render(request, 'catalog/home.html', context={'num_books': num_books, 'num_authors': num_authors,
                                                'num_genres': num_genres, 'num_visits': num_visits})


def addAuthor(request):
    """implementacja formy na stronie z listą autorów"""
    author = Author.objects.all()
    authorsform = AuthorForm()
    return render(request, "catalog/add_author.html", {'form': authorsform, 'author': author})


def createAuthor(request):
    """tworzenie nowego autora"""
    if request.method == "POST":
        author = Author()
        author.name = request.POST.get("name")
        author.nationality = request.POST.get("nationality")
        author.date_of_birth = request.POST.get("date_of_birth")
        author.save()
        return HttpResponseRedirect("/add_author/")


def delAuthor(request, id):
    """usuwanie autora"""
    try:
        author = Author.objects.get(id=id)
        author.delete()
        return HttpResponseRedirect("/add_author/")
    except Author.DoesNotExist:
        return HttpResponseNotFound("<h2>Authora nie znaleziono</h2>")


def editAuthor(request, id):
    """edytowanie autora z przekierowaniem"""
    author = Author.objects.get(id=id)
    if request.method == "POST":
        author.name = request.POST.get("name")
        author.nationality = request.POST.get("nationality")
        author.date_of_birth = request.POST.get("date_of_birth")
        # author.date_of_death = request.POST.get("date_of_death")
        author.save()
        return HttpResponseRedirect("/add_author/")
    else:
        return render(request, "catalog/edit_author.html", {"author": author})


class BookCreate(CreateView):
    """tworzenie książki z wykożystaniwm widoku generycznego
       templatka powinna mieć nazwe: model_name_form.html"""
    model = Book
    fields = '__all__'
    success_url = reverse_lazy('books')


class BookUpdate(UpdateView):
    """widok generyczny UpdateView"""
    model = Book
    fields = '__all__'
    success_url = reverse_lazy('books')


class BookDelete(DeleteView):
    """nazwa templatki musi być: model_name_confirm_delete.html"""
    model = Book
    success_url = reverse_lazy('books')


class BookListView(generic.ListView):
    """generic view wyciąga dane z bazy modeli Book, po czym wypełnia templatkez listą książek
       templatka powinna mieć nazwe: nazwa_modeli_list.html"""
    model = Book
    paginate_by = 3


class BookDetailView(generic.DetailView):
    """generic view dla prezentowania detali książki przez templatke book_detail.html"""
    model = Book


class AuthorListView(generic.ListView):
    """generic view wyciąga dane z bazy modeli Author, po czym wypełnia templatke z listą autorów"""
    model = Author
    paginate_by = 3


class AuthorDetailView(generic.DetailView):
    """generic view dla prezentowania detali autora przez templatke author_detail.html"""
    model = Author
