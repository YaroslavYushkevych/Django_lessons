from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .models import *

# Create your views here.
menu = [{'title': "Про сайт", 'url_name': 'about'},
        {'title': "Додати статтю", 'url_name': 'add_page'},
        {'title': "Зворотній зв'язок", 'url_name': 'contact'},
        {'title': "Зайти", 'url_name': 'login'}
]


def index(request):
    posts = Women.objects.all()

    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Головна сторінка',
        'cat_selected': 0,
    }

    return render(request, 'women/index.html', context=context)


def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'Про сайт'})


def addpage(request):
    return HttpResponse("Додавання статті")


def contact(request):
    return HttpResponse("Зворотній зв'язок")


def login(request):
    return HttpResponse("Авторизация")


def show_post(request, post_id):
    return HttpResponse(f"Відображення статті с id = {post_id}")


def show_category(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id)

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Відображення по групам',
        'cat_selected': cat_id,
    }

    return render(request, 'women/index.html', context=context)











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