from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Сторінка додатку women.")

def categories(request):
    return HttpResponse("<h1>Статті по категоріям</h1>")

def index_adm(request):
    return HttpResponse("<h1>Сторінка Адміністратора додатку women</h1>")