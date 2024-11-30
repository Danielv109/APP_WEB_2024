"""
URL configuration for proyectoUTDdjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from mainapp import views
from articulos import views
#Manejador de errores 404
from django.conf.urls import handler404
# Para la vista personalizada de 404
from mainapp import views
from django.conf import settings

# Vista personalizada para manejar errores 404
handler404 = 'mainapp.views.page404'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainapp.urls')),
    # path('mainapp/', include('mainapp.urls')), 
    path('', include('articulos.urls')),
    # path('articulos/', include('articulos.urls')), 
]

# ruta de imagenes
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    