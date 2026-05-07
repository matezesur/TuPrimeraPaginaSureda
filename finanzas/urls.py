from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('articulos/', views.lista_articulos, name='lista_articulos'),
    path('articulos/crear/', views.crear_articulo, name='crear_articulo'),
    path('servicios/', views.lista_servicios, name='lista_servicios'),
    path('servicios/crear/', views.crear_servicio, name='crear_servicio'),
    path('consultas/', views.lista_consultas, name='lista_consultas'),
    path('consultas/crear/', views.crear_consulta, name='crear_consulta'),
    path('buscar/', views.buscar_articulos, name='buscar_articulos'),
]
