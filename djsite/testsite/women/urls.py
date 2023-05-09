from django.urls import path

from .views import *

urlpatterns = [
    path('women_2/', index),
    path('cats/', categories),
    path('', index_adm),
]