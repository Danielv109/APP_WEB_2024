from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from articulos.models import Category, Article

# Crear tus vistas aquí.

@login_required(login_url='inicio')
def listado_art(request):
    # Sacar todos los artículos de la base de datos
    articles = Article.objects.all()

    return render(request, 'articulos/listado_art.html', {
        'title': 'Artículos',
        'content': 'Listado de Artículos',
        'articles': articles  # Agregar la coma aquí
    })


@login_required(login_url='inicio')
def listado_cat(request):
    # Sacar todas las categorías de la base de datos
    categories = Category.objects.all()

    return render(request, 'categorias/listado_cat.html', {
        'title': 'Categorías',
        'content': 'Listado de Categorías',
        'categories': categories  # Agregar la coma aquí
    })
