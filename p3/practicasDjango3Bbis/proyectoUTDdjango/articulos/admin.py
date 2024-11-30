from django.contrib import admin
from .models import Category, Article

# Configuración de la administración para Category
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')  # Campos de solo lectura
    search_fields = ('name', 'descripcion')  # Campos para el buscador
    list_display = ('name', 'descripcion', 'created_at')  # Campos mostrados en la lista
    ordering = ('-created_at',)  # Orden descendente por fecha de creación

# Configuración de la administración para Article
class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('user', 'created_at', 'updated_at')  # Campos de solo lectura
    search_fields = ('title', 'content', 'user__username', 'categories__name')  # Campos para el buscador
    list_filter = ('public', 'user', 'categories')  # Filtros laterales
    list_display = ('title', 'public', 'user', 'created_at')  # Campos mostrados en la lista
    ordering = ('-created_at',)  # Orden descendente por fecha de creación

    # Sobrescribir el método save_model para asignar automáticamente el usuario autenticado
    def save_model(self, request, obj, form, change):
        if not obj.user_id:  # Si el artículo no tiene un usuario asignado
            obj.user_id = request.user.id
        obj.save()

# Registro de los modelos en el panel de administración
admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)  # Registrar el modelo Article con la configuración ArticleAdmin en el panel de administración
