from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta
# Create your models here.
class Evento(models.Model): # tabela
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField(verbose_name='Data_do evento')
    data_criacao = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    local = models.CharField(max_length=300, blank=True)

    class Meta: # metadados
        db_table = 'evento' # nome da tabela no banco de dados

    def __str__(self):
        return self.titulo
    def get_data(self):
        return self.data_evento.strftime('%d/%m/%y %H:%M Hrs')
    def get_data_input_evento(self):
        return self.data_evento.strftime('%Y-%m-%dT%H:%M')


    def get_evento_color(self): # retorna cores para o texto da agenda
        if self.data_evento < datetime.now():# vermelho para os eventos passados
            return 'red'
        if  self.data_evento < datetime.now() + timedelta(hours=1) and self.data_evento > datetime.now():# amarelo para os eventos proximos
            return '#ffbb00'
        else:
            return ''