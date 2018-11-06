"""loja_automoveis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from carros import views

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    #path('cores/', views.listar_cores, name="cores"),
    path('', views.index, name="index"),
    path('home/', views.index, name="home"),
    path('sobre/', views.sobre_carros, name="sobre"),
    path('montadora/', views.montadoras, name="montadora"),
    path('montadora/cadastrar', views.montadora_cadastrar, name="cadastrar_montadora"),
    path('montadora/<int:opcao>', views.montadoras, name="montadoralista"),
    path('montadora/editar/<int:id>', views.montadora_editar, name="editar_montadora"),
    path('cores/', views.mostrar_cores, name="cores"),
    path('cores/<int:opcao>', views.mostrar_cores, name="cores_opcao"),
    path('cores/cadastrar/', views.cores_cadastrar, name="cores_cadastrar"),
    path('cores/editar/<int:id>', views.cores_editar, name="cores_editar"),
]
