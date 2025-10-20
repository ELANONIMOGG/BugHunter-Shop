from django.urls import path
from . import views

app_name = 'productos'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('categoria/<slug:slug>/', views.categoria_productos, name='categoria'),
    path('producto/<slug:slug>/', views.detalle_producto, name='detalle_producto'),
]