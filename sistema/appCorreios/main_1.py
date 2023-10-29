from models import *
#from appCorreios.models import *

#model de pessoa

pessoa = Pessoa(nome = "Marcos", email= "marcos@gmail")
pessoa.save()

#model de endereco

endereco = Endereco(cidade= "Rio de Janeiro", uf= "RJ", bairro= 'Ricardo de Albuquerque',
                    logradouro= 'JUrubeba', cep= '256478-77', complemento= 'lote 5 casa 1')

endereco.pessoa= pessoa
endereco.save()

#models telefone

tel1= Telefone(tipo= 1, numero = 25897-63214)
tel2= Telefone(tipo= 2, numero = 12345-89214)

tel1.pessoa= pessoa
tel2.pessoa = pessoa

tel1.save()
tel2.save()

Pessoa.objects.all()
Endereco.objects.all()
Telefone.objects.all()

pessoa_consultada = Pessoa.objects.filter(codigo = 1) .first()

pessoa_consultada.endereco = Endereco.objects.filter(pessoa = pessoa_consultada).first()

telefones = Telefone.objects.filter(pessoa = pessoa_consultada)

pessoa_consultada.telefones = telefones

print('-------------------')
print(pessoa_consultada)
print(pessoa_consultada.endereco)
print(pessoa_consultada.telefones)