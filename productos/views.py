from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from productos.models import Barra
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class CrearBarra(CreateView):
    model = Barra
    template_name = "productos/crear_barra.html"
    success_url = reverse_lazy("productos:listado_barras")
    fields = ["modelo", "marca", "peso"]

class ListadoBarras(ListView):
    model = Barra
    template_name = "productos/listado_barras.html"
    context_object_name = "barras"

class VerBarra(DetailView):
    model = Barra
    template_name = "productos/ver_barra.html"

class EditarBarra(LoginRequiredMixin, UpdateView):
    model = Barra
    template_name = reverse_lazy("productos/editar_barra.html")
    success_url = ["modelo", "marca", "peso"]

class EliminarBarra(LoginRequiredMixin, DeleteView):
    model = Barra
    template_name = "productos/eliminar_barra.html"
    success_url = reverse_lazy("productos:listado_barras")