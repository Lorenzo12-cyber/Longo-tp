from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as django_login

def login(request):

    formulario = AuthenticationForm()

    if request.method =="POST":
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.get_user()

            django_login(request, usuario)

            return redirect("inicio:inicio")

    return render(request, "usuarios/login.html", {"form": formulario})


def register(request):

    formulario = ""

    return render(request, "usuarios/register.html", {"form": formulario})