from django.urls import path
from productos import views

app_name = "productos"

urlpatterns = [
    path("barras/", views.ListadoBarras.as_view(), name="listado_barras"),
    path("barras/crear/", views.CrearBarra.as_view(), name="crear_barra"),
    path("barras/<int:pk>/", views.VerBarra.as_view(), name="ver_barra"),
    path("barras/<int:pk>/editar/", views.EditarBarra.as_view(), name="editar_barra"),
    path("barras/<int:pk>/eliminar/", views.EliminarBarra.as_view(), name="eliminar_barra"),
]
