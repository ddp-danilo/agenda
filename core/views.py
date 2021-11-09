from django.shortcuts import render, HttpResponse, redirect
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from datetime import datetime, timedelta
from django.http.response import Http404, JsonResponse

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
    data_atual_mn1h = datetime.now() - timedelta(hours=1)# data atual menos uma hora.
    usuario = request.user
    if request.GET.get('hist') == 'True':
        evento = Evento.objects.filter(usuario=usuario, data_evento__lt=data_atual_mn1h)
        template = 'hist.html'
    else:
        evento = Evento.objects.filter(usuario=usuario, data_evento__gt=data_atual_mn1h)
        template = 'agenda.html'
    dados = {'eventos':evento}
    return render(request, template, dados)

@login_required(login_url='/login')
def evento(request):
    id_evento = request.GET.get('id')
    dados = {}
    if id_evento:
        dados['evento'] = Evento.objects.get(id=id_evento)
    return render(request, 'evento.html', dados)

@login_required(login_url='/login')
def submit_evento(request):
    if request.POST:
        data_evento = request.POST.get('data_evento')
        if data_evento == "":
            messages.error(request, "A data do evento não pode estar vazia!")
            return redirect('/agenda/eventos')
        titulo = request.POST.get('titulo')

        descricao = request.POST.get('descricao')
        usuario = request.user
        local = request.POST.get('local')
        id_evento = request.POST.get('id_evento')
        if id_evento:
            evento = Evento.objects.get(id=id_evento)
            if evento.usuario == usuario:
                evento.data_evento = data_evento
                evento.titulo = titulo
                evento.descricao = descricao
                evento.local = local
                evento.save()
#            Evento.objects.filter(id=id_evento).update(titulo=titulo,
#                                                        data_evento=data_evento,
#                                                        descricao=descricao,
#                                                        local=local)
        else:
            Evento.objects.create(titulo=titulo,
                                  data_evento=data_evento,
                                  descricao=descricao,
                                  usuario=usuario,
                                  local=local)
    return redirect('/')
@login_required(login_url='/login')
def delete_evento(request, id_evento):
    usuario = request.user
    try:
        evento = Evento.objects.get(id=id_evento)
    except Exception:
        print('ok')#debug
        raise Http404
    if evento.usuario == usuario:
        evento.delete()
    else:
        print('ok')  # debug
        raise Http404
    return redirect('/')

@login_required(login_url='/login')
def json_lista_evento(request):
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario).values('id', 'titulo')
    return JsonResponse(list(evento), safe=False)


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