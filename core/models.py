from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Evento(models.Model): # tabela
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField(verbose_name='Data_do evento')
    data_criacao = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta: # metadados
        db_table = 'evento' # nome da tabela no banco de dados

    def __str__(self):
        return self.titulo
    def get_data(self):
        return self.data_evento.strftime('%d/%m/%y %H:%M Hrs')
