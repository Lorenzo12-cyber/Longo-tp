from django.urls import path
from productos import views

app_name = "productos"

urlpatterns = [
    path("barra/crear/", views.crear_barra, name="crear_barra")
]
