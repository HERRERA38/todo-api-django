from django.contrib import admin
from .models import Tarea


@admin.register(Tarea)
class TareaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'usuario', 'completada', 'fecha_caducidad', 'fecha_creacion')
    list_filter = ('completada', 'fecha_creacion')
    search_fields = ('nombre', 'descripcion')