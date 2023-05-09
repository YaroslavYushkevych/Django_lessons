from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('women/', index, name = "home"),
    path('', index_adm),
    path('cats/<slug:catid>/', categories),
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive),
]