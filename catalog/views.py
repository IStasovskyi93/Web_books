from django.shortcuts import render
from django.http import *


def index(request):
    return HttpResponse('<h3>Strona główna "Swiatu ksążek"</h3>')
