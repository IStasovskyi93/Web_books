# Generated by Django 4.0.3 on 2022-03-26 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_remove_bookinpaper_book_bookinpaper_book'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookinpaper',
            name='book',
        ),
        migrations.AddField(
            model_name='book',
            name='book',
            field=models.ManyToManyField(to='catalog.bookinpaper', verbose_name='Książka'),
        ),
    ]