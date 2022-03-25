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
    name = models.CharField(max_length=100, unique=True)
    nationality = models.CharField(verbose_name="Narodowość autora")
    date_of_birth = models.DateField()
    date_of_death = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=150, )
    type = models.CharField(choices=(('eBook', 'eBook'), ('paper', 'paper')), verbose_name="Format książki")
    available = models.IntegerField(help_text="Ilość papierowych egzemplarów.")
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    genre =


class BookCard(models.Model):
    is_paper = models.ForeignKey(Book.type)
    price_net = models.DecimalField(decimal_places=4, max_digits=2)
    quantity = models.IntegerField(default=0)


class

class Comment(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)




# class Category(models.Model):




# class Author
# class Language
# class Comment
# class BookCard
# class User
# class Card
# class Payment