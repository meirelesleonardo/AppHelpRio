# -*- encoding: utf-8 -*-

from django.urls import path, re_path
from . import views

app_name = 'ficha_imovel'

urlpatterns = [

    # The home page
    path('ficha_imovel_criar', views.criar, name='criar'),   

]
