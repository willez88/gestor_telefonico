from django.contrib import admin
from .models import Perfil

class PerfilAdmin(admin.ModelAdmin):
    list_display = ('telefono','user','users',)
    list_filter = ('telefono',)
    ordering = ('telefono',)
    search_fields = ('telefono',)


## Registra el modelo AnhoRegistro en el panel administrativo
admin.site.register(Perfil, PerfilAdmin)
