from django.shortcuts import render, HttpResponse, redirect
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_user(request):
    return render(request, 'login.html')
def logout_user(request):
    logout(request)
    return redirect('/')
def submit_login(request):
    if request.POST:
        username = request.POST.get('use')
        password = request.POST.get('pass')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, 'Usuário ou senha inválido')
    return redirect('/')

@login_required(login_url='/login/')
def lista_eventos(request):
    usuario = request.user  # puxa o usuario que está abrindo a pagina
    # evento = Evento.objects.get(id=1) # puxa Um item especifico da lista Evento
    # evento = Evento.objects.all() # puxo uma lista com todos os itens de Evento
    evento = Evento.objects.filter(usuario=usuario) # puxa somente os ítens da tabela Evento que pertencem ao usuario atual
    dados = {'eventos':evento}
    return render(request, 'agenda.html', dados)

@login_required(login_url='/login')
def evento(request):
    return render(request, 'evento.html')

@login_required(login_url='/login')
def add_evento(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        data_evento = request.POST.get('data_evento')
        descricao = request.POST.get('descricao')
        usuario = request.user
        Evento.objects.create(titulo=titulo,
                              data_evento=data_evento,
                              descricao=descricao,
                              usuario=usuario)

    return redirect('/')


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
    paginas = ['admin','agenda','teste',]
    #url = ''
    #for pagina in paginas:
    #    url += '<a href="/{}">{}</a></br>'.format(pagina, pagina)
    #return HttpResponse(url paginas)
    dados = {'paginas':paginas}
    return render(request, 'mapa.html', dados)