from django.urls import path
from inicio.views import inicio, vista_datos1, primer_template, segundo_template, crear_pesa

app_name = "inicio"

urlpatterns = [
    path("", inicio, name="inicio"),
    path("vista-datos1/<nombre>/", vista_datos1, name="vista_datos1"),
    path("primer-template/", primer_template, name="primer_template"),
    path("segundo-template/", segundo_template, name="segundo_template"),
    path("crear-pesa/<marca>/<material>/<peso>/", crear_pesa, name="crear_pesa")
]

   