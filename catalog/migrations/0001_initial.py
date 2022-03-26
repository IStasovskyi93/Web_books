# Generated by Django 4.0.3 on 2022-03-26 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Imię i nazwisko autora')),
                ('nationality', models.CharField(max_length=30, verbose_name='Narodowość')),
                ('date_of_birth', models.DateField(verbose_name='Data urodzenia')),
                ('date_of_death', models.DateField(blank=True, help_text='Nie obowjąnzkowe', null=True, verbose_name='Data smierci')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Tytuł książki')),
                ('summary', models.TextField(max_length=1000, verbose_name='Opis')),
                ('isbn', models.CharField(help_text='Powinien mieścić 13 znaków', max_length=13, verbose_name='ISBN')),
                ('ebook_price', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Cena wersji elektronicznej')),
                ('paper_price', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Cena papierowej wersji')),
                ('authors', models.ManyToManyField(help_text='Wybież autora tworu', to='catalog.author', verbose_name='Autor(zy)')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='Kategoria')),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Język tworu', max_length=30, unique=True, verbose_name='Language')),
            ],
        ),
        migrations.CreateModel(
            name='BookInPaper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0, verbose_name='Ilość egzemplarów')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.book', verbose_name='Książka')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.language', verbose_name='Język ksiązki'),
        ),
    ]
