from django.shortcuts import render

# Create your views here.

def index(request):
    mensaje='Hola soy un mensaje'
    return render(request, 'mainapp/index.html', {
        'title': 'Inicio',
        'content': '.::!Bienvenido a la Pagina Principal!::.',
        'mensaje': mensaje,
    })

def about(request):
    return render(request, 'mainapp/about.html', {
        'title': 'Acerca de Nosotros',
        'content': 'Somos un equipo de Desarrollo de SW',
    })

def mision(request):
    return render(request, 'mainapp/mision.html', {
        'title': 'Nuestra Mision',
        'content': 'Nuestra Mision es ser el mejor equipo de Desarrollo de SW en el mundo',
    })

def vision(request):
    return render(request, 'mainapp/vision.html', {
        'title': 'Nuestra Vision',
        'content': 'Nuestra Vision es ser el mejor equipo de Desarrollo de SW  en el mundo',
    })