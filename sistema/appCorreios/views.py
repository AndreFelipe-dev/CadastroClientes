from django.shortcuts import render

from .forms import CadastroForm
from .models import *


HOME_PAGE = 'appCorreios/home.html'
CADASTRO_PAGE = 'appCorreios/cadastro.html'
LISTA_PAGE = 'appCorreios/lista.html'


def home(request):
    return render(request,HOME_PAGE)

pass


def cadastro(request):

    form = CadastroForm()
    return render(request,CADASTRO_PAGE, {'form': form})
    pass

def lista(request):

    pessoas = Pessoa.objects.all()
    return render(request, LISTA_PAGE, {'pessoas': pessoas})

    pass

def cadastrar(request):

    try:

        if request.method== 'POST':
            form = CadastroForm(request.POST)
            if form.is_valid():

                pessoa = Pessoa()
                endereco = Endereco()
                tel1 = Telefone()
                tel2 = Telefone()

                pessoa.nome = form.cleaned_data['nome']
                pessoa.email = form.cleaned_data['email']

                endereco.uf = form.cleaned_data['endereco']
                endereco.cidade = form.cleaned_data['cidade']
                endereco.bairro = form.cleaned_data['bairro']
                endereco.logradouro = form.cleaned_data['logradouro']
                endereco.cep = form.cleaned_data['cep']

                if form.cleaned_data['complemento'] is not None:

                    endereco.complemento = form.cleaned_data['complemento']

                else:
                    endereco.complemento= 'Não informado'

                pessoa.save()
                endereco.pessoa=pessoa
                pessoa.save()

                if form.cleaned_data['numero1'] is not None:
                    tel1.numero= form.cleaned_data['numero1']
                    tel1.Tipo= 1
                    tel1.pessoa=pessoa
                    tel1.save()

                if form.cleaned_data['numero2'] is not None:
                    tel2.numero = form.cleaned_data['numero2']
                    tel2.Tipo = 2
                    tel2.pessoa = pessoa
                    tel2.save()

                msg = 'Dados gravados com sucesso.'
                return render(request,CADASTRO_PAGE ,{'msg': msg , 'form': CadastroForm()})



            else :
                raise Exception('Erros %S.', form.errors)

        else :
                raise Exception('MethodEnvioError,use POST para formulários')

    except Exception as ex:
         msg = ex.args
    return render(request, CADASTRO_PAGE ,{'msg': msg, 'form': CadastroForm()}, )


    pass