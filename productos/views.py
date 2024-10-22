from django.shortcuts import render
from django.http import HttpResponse

def crear_barra(request):
    return HttpResponse("Crear barra")
