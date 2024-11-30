from django.urls import path
from . import views  

urlpatterns = [
    path('listado_articulos/', views.listado_art, name='listado_articulos'),
    path('listado_categorias/', views.listado_cat, name='listado_categorias'),

]
