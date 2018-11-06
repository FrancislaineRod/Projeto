from django.shortcuts import render
from django.http import HttpResponse

from carros.forms import CorForm
from .models import *
from django.views.generic import TemplateView
import pdb;
from django.shortcuts import render, get_object_or_404, redirect
from .forms import MontadoraForm
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def listar_cores(request):
    carros = Carro.objects.all()
    string = ''
    for carro in carros:
        string += "Placa: " + carro.placa + "<br>"
        string += "Modelo: " + carro.modelo.montadora.sigla + " - " + carro.modelo.nome + "<br>"
        string += "Valor do veículo: R$" + str(carro.modelo.valor) + "<br>"
        valor_total = carro.modelo.valor
        string += "Itens:<br>"
        for linha in carro.itens_escolhidos.all():
            string += " &emsp; - " + linha.item.descricao

            if (linha.item_serie):
                string += " [Item de série]"
            else:
                string += " [R$ " + str(linha.item.valor) + "]"
                valor_total += linha.item.valor
            string += "<br>"

        string += "Valor <b>TOTAL</b> veículo: R$" + str(valor_total) + "<br>"
        string += "<hr>"

    return HttpResponse(string)


def sobre_carros(request):
    contexto = {
        "nome_aula": "AULA DE TEMPLATESSSSSSSSSS",
        "data_atual": "27/09/2018",
        "carros": Carro.objects.all()
    }
    # dicionario
    # vetor com indices LITERAIS
    return render(request, '../templates/sobre.html', contexto)


@csrf_exempt
def montadoras(request, opcao=None):
    if opcao == 1:
        opcao_mensagem = 'Montadora editada com sucesso!'
    else:
        if opcao == 2:
            opcao_mensagem = 'Montadora cadastrada com sucesso!'
        else:
            opcao_mensagem = None

    if request.method == 'POST':
        idmontadora = request.POST.get('id')
        temp = Montadora.objects.get(id=idmontadora)
        opcao_mensagem = 'Montadora ' + temp.sigla + ' - ' + temp.descricao + ' removida com sucesso!'
        temp.delete()
        opcao = True

    contexto = {
        "montadoras": Montadora.objects.all(),
        'opcao': opcao,
        'opcao_mensagem': opcao_mensagem
    }
    # dicionario
    # vetor com indices LITERAIS
    return render(request, '../templates/montadora.html', contexto)


def index(request):
    contexto = {
        ""
    }
    return render(request, '../templates/inicial.html')


def montadora_editar(request, id):
    montadora = get_object_or_404(Montadora, id=id)

    # APENAS UM
    if request.method == 'POST':
        montadora.descricao = request.POST.get('descricao')
        montadora.sigla = request.POST.get('sigla')
        montadora.save()
        return redirect('montadoralista', opcao=1)

    else:
        contexto = {
            'montadora': montadora
        }
    return render(request, '../templates/montadora_editar.html', contexto)


def montadora_cadastrar(request):
    form = MontadoraForm(request.POST or None)
    if form.is_valid() and request.POST:
        form.save()
        return redirect('montadoralista', opcao=2)
    contexto = {
        "formMontadora": form,
    }
    return render(request, '../templates/montadora_cadastrar.html', contexto)


@csrf_exempt
def mostrar_cores(request, opcao=None):
    if opcao == 1:
        opcao_mensagem = 'Cor cadastrada com sucesso!'
    else:
        if opcao == 2:
            opcao_mensagem = 'Cor editada com sucesso!'
        else:
            if opcao==3:
                opcao_mensagem = "Cor removida com sucesso"
            else:
                opcao_mensagem = None


    if request.method == 'POST':
        idcor = request.POST.get('id')
        temp = Cor.objects.get(id=idcor)
        temp.delete()
       # opcao = True

    contexto = {
        "cores": Cor.objects.all(),
        "opcao":opcao,
        "opcao_mensagem":opcao_mensagem

    }
    return render(request, '../templates/cores.html', contexto)


def cores_cadastrar(request):
    form = CorForm(request.POST or None)
    if form.is_valid() and request.POST:
        form.save()
        return redirect('cores')
    contexto = {
        "formCor": form,
    }
    return render(request, '../templates/cores_cadastrar.html', contexto)


'''
def cores_editar(request,id):
    cor = get_object_or_404(Cor, id=id)

    # APENAS UM
    if request.method == 'POST':
        cor.descricao = request.POST.get('descricao')
        cor.valor = request.POST.get('valor')
        cor.save()
        return redirect('cores')

    else:
        contexto = {
            'cores': cor
        }
    return render(request, '../templates/cores_editar.html', contexto)
'''


def cores_editar(request, id):
    cor = get_object_or_404(Cor, id=id)
    form = CorForm(request.POST or None, instance=cor)
    # APENAS UM
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('cores_opcao',opcao = 2)
    else:
        contexto = {
            'cores': cor,
            'form': form
        }
    return render(request, '../templates/cores_editar.html', contexto)
