from django.db import models
from django.contrib.auth.models import User

# Modelo para Categorías
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')  # Nombre de la categoría
    descripcion = models.CharField(max_length=255, verbose_name='Descripcion')  # Descripción de la categoría
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')  # Fecha de creación
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Actualizado el')  # Fecha de última actualización

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.name

# Modelo para Artículos
class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name='Titulo')  # Título del artículo
    content = models.TextField(verbose_name='Contenido')  # Contenido del artículo
    image = models.ImageField(default='null', verbose_name='Imagen', upload_to="articles")  # Imagen asociada al artículo
    public = models.BooleanField(verbose_name="¿Visible?")  # Visibilidad pública del artículo
    user = models.ForeignKey(User, editable=False, verbose_name='Usuario', on_delete=models.CASCADE)  # Relación con el usuario
    categories = models.ManyToManyField(Category, verbose_name='Categorias', blank=True)  # Categorías asociadas
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado el")  # Fecha de creación
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Actualizado el")  # Fecha de última actualización

    class Meta:
        verbose_name = "Articulo"
        verbose_name_plural = "Articulos"
        ordering = ['-created_at']  # Ordenar por fecha de creación descendente

    def __str__(self):
        return self.title
