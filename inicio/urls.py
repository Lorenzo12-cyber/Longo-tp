from django.urls import path
from inicio.views import inicio, primer_template, segundo_template, crear_pesa, buscar_pesa

app_name = "inicio"

urlpatterns = [
    path("", inicio, name="inicio"),
    path("primer-template/", primer_template, name="primer_template"),
    path("segundo-template/", segundo_template, name="segundo_template"),
    path("crear-pesa/<marca>/<material>/<peso>/", crear_pesa, name="crear_pesa"),
    path("buscar-pesa/", buscar_pesa, name="buscar_pesa"),
    path("crear-pesa/", crear_pesa, name="crear_pesa"),
]

   