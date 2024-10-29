from django.http import HttpResponse
from django.template import Template, Context, loader
from datetime import datetime
from django.shortcuts import render, redirect
from inicio.models import Pesas 
from inicio.forms import CrearPesaFormulario, BuscarPesaFormulario, EditarPesaFormulario
from django.contrib.auth.decorators import login_required

def inicio(request):
    return render(request, "inicio/index.html")

def acerca_de_mi(request):

    archivo_del_template = open(r"templates\acerca_de_mi.html")
    template = Template(archivo_del_template.read())
    archivo_del_template.close()
    contexto = Context()

    render_template = template.render(contexto)

    return HttpResponse(render_template) 

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


def ver_pesa(request, id):
    pesa = Pesas.objects.get(id=id)
    return render(request, "inicio/ver_pesa.html", {"pesa": pesa})

@login_required
def eliminar_pesa(request, id):
    pesa = Pesas.objects.get(id=id)
    pesa.delete()
    return redirect("inicio:buscar_pesa")
@login_required
def editar_pesa(request, id):
    pesa = Pesas.objects.get(id=id)

    formulario = EditarPesaFormulario(initial={"material": pesa.material, "marca": pesa.marca, "peso": pesa.peso})

    if request.method == "POST":
        formulario = EditarPesaFormulario(request.POST)
        if formulario.is_valid():
            pesa.material = formulario.cleaned_data.get("material")
            pesa.marca = formulario.cleaned_data.get("marca")
            pesa.peso = formulario.cleaned_data.get("peso")

            pesa.save()

            return redirect("inicio:buscar_pesa")
    return render(request, "inicio/editar_pesa.html", {"pesa": pesa, "form": formulario})