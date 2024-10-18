from django.http import HttpResponse
from django.template import Template, Context, loader
from datetime import datetime
from django.shortcuts import render, redirect
from inicio.models import Pesas 
from inicio.forms import CrearPesaFormulario, BuscarPesaFormulario

def inicio(request):
    return render(request, "inicio/index.html")

def primer_template(request):

    archivo_del_template = open(r"templates\primer_template.html")
    template = Template(archivo_del_template.read())
    archivo_del_template.close()
    contexto = Context()

    render_template = template.render(contexto)

    return HttpResponse(render_template) 

def segundo_template(request):

    fecha_actual = datetime.now()
    datos = {
        "fecha_actual": fecha_actual,
    }

    return render(request, "inicio/segundo_template.html", datos)


def buscar_pesa(request):

    formulario = BuscarPesaFormulario(request.GET)
    if formulario.is_valid():
        marca = formulario.cleaned_data.get("marca") 
        pesas = Pesas.objects.filter(marca__icontains=marca)

    return render(request, "inicio/buscar_pesa.html", {"pesas": pesas, "form": formulario})

def crear_pesa(request):

    formulario = CrearPesaFormulario()

    if request.method == "POST":
  
        formulario = CrearPesaFormulario(request.POST)
        if formulario.is_valid(): 
            data = formulario.cleaned_data 
            pesa = Pesas(marca=data.get("marca"), material=data.get("material"), peso=data.get("peso"))
            pesa.save()
            return redirect("inicio:buscar_pesa") 

    return render(request, "inicio/crear_pesa.html", {"form": formulario})