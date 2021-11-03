from django.contrib import admin
from core.models import Evento
# Register your models here.
class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_evento', 'data_criacao')# indica como a tabela vai aparecer no django admin
    list_filter = ('titulo', 'usuario', 'data_criacao',) # adciona filtros no django adminstrator.

admin.site.register(Evento, EventoAdmin)
