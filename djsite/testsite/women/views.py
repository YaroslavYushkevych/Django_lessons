from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import *
from .models import *
from .utils import *

# Create your views here.


class WomenHome(DataMixin, ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'
    #extra_context = {'title': 'Главная страница'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Головна сторінка")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Women.objects.filter(is_published=True)




def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'Про сайт'})


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'women/addpage.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')
    raise_exception = True


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Додавання статті")
        return dict(list(context.items()) + list(c_def.items()))

def contact(request):
    return HttpResponse("Зворотній зв'язок")


def login(request):
    return HttpResponse("Авторизація")

class ShowPost(DataMixin, DetailView):
    model = Women
    template_name = 'women/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))


class WomenCategory(DataMixin, ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Women.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Категорія - ' + str(context['posts'][0].cat),
                                      cat_selected=context['posts'][0].cat_id)

        return dict(list(context.items()) + list(c_def.items()))








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