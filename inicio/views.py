from django.http import HttpResponse
from django.template import Template, Context, loader
from datetime import datetime
from django.shortcuts import render 
from inicio.models import Pesas 

def inicio(request):
    return render(request, "inicio/index.html")

def vista_datos1(request, nombre):
    nombre_mayuscula = nombre.upper()
    return HttpResponse(f"Hola {nombre_mayuscula}!!")

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
        "numeros": list(range(1, 11))
    }

    return render(request, "inicio/segundo_template.html", datos)

def crear_pesa(request, marca, material, peso):

    pesa = Pesas(marca=marca, material=material, peso=peso)
    pesa.save()
    return render(request, "inicio/creacion_pesa.html", {"pesa": pesa})