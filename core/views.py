from django.shortcuts import render, HttpResponse
from core.models import Evento
def test(request):
    tst = Evento.objects.count()
    return HttpResponse('{}'.format(tst))

def lista_evento(request):
    num_linhas = Evento.objects.count()
    url = ''
    for n in range(1, num_linhas + 1):
        evento = Evento.objects.get(id=n)
        url += '<a href="/evento/{}">{}</a></br>'.format(evento.titulo, evento.titulo)
    return HttpResponse(url)
def mostra_evento(request, titulo_evento):
    evento = Evento.objects.get(titulo=titulo_evento)
    return HttpResponse('Evento: {} </br> Descriçao:  {} </br> Data do Evento: {}'.format(evento.titulo,
                                                                                         evento.descricao,
                                                                                         evento.data_evento,))
def mapa(request):
    paginas = ['admin','lista/Evento','teste']
    url = ''
    for pagina in paginas:
        url += '<a href="/{}">{}</a></br>'.format(pagina, pagina)
    return HttpResponse(url)
