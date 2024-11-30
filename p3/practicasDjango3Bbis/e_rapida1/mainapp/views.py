from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'mainapp/index.html', {
        'title': 'Menu de Inicio',
        'content': 'Bienvenido a la Pagina Principal de nuestra empresa',
    })

def about(request):
    return render(request, 'mainapp/about.html', {
        'title': 'Acerca de Nuestra empresa',
        'content': 'Somos una empresa lista para ayudarlos',
    })

def mision(request):
    return render(request, 'mainapp/mision.html', {
        'title': 'Nuestra Mision',
        'content': 'Nuestra Mision es ayudar a todas las personas posibles',
    })

def vision(request):
    return render(request, 'mainapp/vision.html', {
        'title': 'Nuestra Vision',
        'content': 'Nuestra Vision es poder tener los recursos para llegar a todas las personas en todo el mundo',
    })

def logines(request):
    return render(request, 'users/logines.html', {
        'title': 'Inicio de Sesión',
        'content': 'Hola que tal',
    })

def registros(request):
    return render(request, 'users/registros.html', {
        'title': 'Favor de Registrarse',
        'content': 'Hola que tal',
    })