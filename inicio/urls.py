from django.urls import path
from inicio.views import (
    inicio,
    buscar_pesa, 
    crear_pesa,
    acerca_de_mi,
    ver_pesa,
    eliminar_pesa,
    editar_pesa
)
app_name = "inicio"

urlpatterns = [
    path("", inicio, name="inicio"),
    path("buscar-pesa/", buscar_pesa, name="buscar_pesa"),
    path("crear-pesa/", crear_pesa, name="crear_pesa"),
    path("acerca-de-mi/", acerca_de_mi, name="acerca_de_mi"),
    path("ver-pesa/", ver_pesa, name="ver_pesa"),
    path("ver-pesa/<int:id>/", ver_pesa, name="ver_pesa"),
    path("eliminar-pesa/<int:id>/", eliminar_pesa, name="eliminar_pesa"),
    path("editar-pesa/<int:id>/", editar_pesa, name="editar_pesa"),
]




   