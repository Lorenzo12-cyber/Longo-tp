from django.urls import path
from inicio.views import inicio, vista_datos1, primer_template, segundo_template, crear_pesa

urlpatterns = [
    path("", inicio),
    path("vista-datos1/<nombre>/", vista_datos1),
    path("primer-template/", primer_template),
    path("segundo-template/", segundo_template),
    path("crear-pesa/<marca>/<material>/<peso>/", crear_pesa)
]

   