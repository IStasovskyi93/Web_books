# Generated by Django 4.0.3 on 2022-04-09 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_remove_book_book_bookinpaper_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='date_of_death',
            field=models.DateField(blank=True, default='', help_text='Nie obowjąnzkowe', null=True, verbose_name='Data smierci'),
        ),
    ]
