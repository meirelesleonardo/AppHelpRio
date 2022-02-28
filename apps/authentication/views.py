# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Create your views here.
from __future__ import print_function
import email
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from apps.instituicao.models import Instituicao
from .forms import LoginForm, SignUpForm


def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                msg = 'Usuário ou senha incorreto'
        else:
            msg = 'Erro na validação do formulário'

    return render(request, "accounts/login.html", {"form": form, "msg": msg})

@login_required(login_url="/login/")
def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        #data = {'Instituicao':['2']}
        
        form = SignUpForm(request.POST)
               
        if form.is_valid():
            novoUsuario = form.save(commit=False)           
            novoUsuario.Instituicao = request.user.Instituicao    
            novoUsuario.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'Usuário criado com sucesso - <a href="/login/">login</a>.'
            success = True

            #return redirect("/login")

        else:
            msg = 'Form is not valid'
    else:
        data = {'Instituicao':request.user.Instituicao}
        form = SignUpForm(data)       
      

    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})
