from django.shortcuts import render, HttpResponse, redirect
from core.models import Evento

#def index(request):    # uma maneira de setar a home do site
#    return redirect('/agenda/')
def test(request):
    # tst = Evento.objects.count()
    # return HttpResponse('{}'.format(tst))
    return HttpResponse('<b>{}</b>'.format(request.user))

#def lista_evento(request): # Meu lista eventos
#    num_linhas = Evento.objects.count()
#    url = ''
#    for n in range(1, num_linhas + 1):
#        evento = Evento.objects.get(id=n)
#        url += '<a href="/evento/{}">{}</a></br>'.format(evento.titulo, evento.titulo)
#    return HttpResponse(url)
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

def lista_eventos(request):
    if not request.user.is_authenticated:
        return HttpResponse('<b>Usuário não logado</b>')
    else:
        usuario = request.user  # puxa o usuario que está abrindo a pagina
        # evento = Evento.objects.get(id=1) # puxa Um item especifico da lista Evento
        # evento = Evento.objects.all() # puxo uma lista com todos os itens de Evento
        evento = Evento.objects.filter(usuario=usuario) # puxa os itens de Evento que pertencen ao usuario atual
        dados = {'eventos':evento}
        return render(request, 'agenda.html', dados)
