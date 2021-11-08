"""agenda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views
from django.views.generic import RedirectView

urlpatterns = [

    path('', RedirectView.as_view(url='/agenda')), # indice sem a necessidade de criar uma view
    path('admin/', admin.site.urls),
    path('evento/<titulo_evento>', views.mostra_evento), # mostra as informações do evento requisitado
    path('mapa/', views.mapa), # um mapa do site
    path('teste/', views.test), # Uma pagina para fazer experimentos
    path('login/', views.login_user),
    path('login/submit', views.submit_login),
    path('logout', views.logout_user),
    path('agenda/', views.lista_eventos),
    path('agenda/lista', views.json_lista_evento),
    path('agenda/eventos/', views.evento),
    path('agenda/eventos/submit', views.submit_evento),
    path('agenda/eventos/delete/<int:id_evento>/', views.delete_evento),
]
