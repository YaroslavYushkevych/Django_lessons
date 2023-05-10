from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .models import *

# Create your views here.
menu = ["Про сайт", "Додати статтю", "Зворотній зв'язок", "Ввійти"]

def index(request):
    posts = Women.objects.all()
    return render(request, 'women/index.html', {'posts': posts, 'menu': menu, 'title': 'Головна сторінка'})


def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'Про сайт'})


def categories(request, catid):
    #Перевірка чи щось було записано
    if(request.GET):
        print(request.GET)
    return HttpResponse(f"<h1>Статті по категоріям</h1>{catid}</p>")

def archive(request, year):
    """Виклик помилки
    if(int(year) > 2023):
        raise Http404()"""
    if (int(year) > 2023):
        #Тимчасовий 302   redirect('/')
        #Постійний  301   redirect('/', permanent=True)
        return redirect('home', permanent=True)
    return HttpResponse(f"<h1>Архів по рокам</h1>{year}</p>")








def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Сторінка не знайдена</h1>'
                                '<h2>Помилка 404</h2>')
def serverError(request):
    return HttpResponseNotFound('<h1>Помилка серверу</h1>'
                                '<h2>Помилка 500</h2>')
def accesForbidden(request, exception):
    return HttpResponseNotFound('<h1>Доступ заборонено</h1>'
                                '<h2>Помилка 403</h2>')
def impossibleProcessRequest(request, exception):
    return HttpResponseNotFound('<h1>Неможливо обробити запит</h1>'
                                '<h2>Помилка 400</h2>')