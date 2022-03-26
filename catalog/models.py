from django.db import models
from django.urls import reverse


class Language(models.Model):
    name = models.CharField(max_length=30, help_text="Język tworu", verbose_name="Language", unique=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name="Kategoria")

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Imię i nazwisko autora")
    nationality = models.CharField(max_length=30, verbose_name="Narodowość")
    date_of_birth = models.DateField(verbose_name="Data urodzenia")
    date_of_death = models.DateField(null=True, blank=True, verbose_name="Data smierci", help_text="Nie obowjąnzkowe")

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=150, verbose_name="Tytuł książki")
    language = models.ForeignKey(Language, on_delete=models.CASCADE, verbose_name="Język ksiązki", null=True)
    authors = models.ManyToManyField(Author, help_text="Wybież autora tworu", verbose_name="Autor(zy)")
    summary = models.TextField(max_length=1000, verbose_name="Opis")
    isbn = models.CharField(max_length=13, help_text="Powinien mieścić 13 znaków", verbose_name="ISBN")
    ebook_price = models.DecimalField(max_digits=4, decimal_places=2, verbose_name="Cena wersji elektronicznej")
    paper_price = models.DecimalField(max_digits=4, decimal_places=2, verbose_name="Cena papierowej wersji")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail', args=[str(self.id)])


class BookInPaper(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name="Książka")
    quantity = models.IntegerField(default=0, verbose_name="Ilość egzemplarów")

    def __str__(self):
        return '%s %s' % (self.book, self.quantity)



# class Order(models.Model):
#     sum_price_net = models.DecimalField(decimal_places=4, max_digits=2)
#     sum_price_gross = models.DecimalField(decimal_places=4, max_digits=2)
#     is_paid = models.ForeignKey('Payment', on_delete=models.DO_NOTHING)
#     pay_time = models.DateTimeField(auto_now_add=True)



# class Basket(models.Model):
#     book = models.ForeignKey(Book, on_delete=models.CASCADE)
#     is_paper = models.BooleanField()
#     price_net = models.DecimalField(decimal_places=4, max_digits=2)
#     price_gross = models.DecimalField(decimal_places=4, max_digits=2)
#     date = models.DateTimeField(auto_now_add=True)

# class User(models.Model):
#     first_name = models.CharField(max_length=20)
#     last_name = models.CharField(max_length=30, null=True)
#     age = models.IntegerField()
#     email = models.EmailField()
#     password =



