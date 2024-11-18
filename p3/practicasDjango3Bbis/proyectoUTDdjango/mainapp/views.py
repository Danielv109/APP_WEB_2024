from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'mainapp/index.html', {
        'title': 'Inicio',
        'content': '.::!Bienvenido a la Pagina Principal!::.',
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

def handler400(request, exception):
    return render(request, 'mainapp/400.html', status=400)

def handler403(request, exception):
    return render(request, 'mainapp/403.html', status=403)

def handler404(request, exception):
    return render(request, 'mainapp/404.html', status=404)

def handler500(request):
    return render(request, 'mainapp/500.html', status=500)
