from models import *
#from appCorreios.models import *
#python manage.py shell
#model de pessoa

pessoa = Pessoa(nome = "João", email= "joao@gmail")
pessoa.save()

#model de endereco

endereco = Endereco(cidade= "Rio de Janeiro", uf= "RJ", bairro= 'taquara',
                    logradouro= 'est.dos  tres rios', cep= '256478-77', complemento= 'casa2')

endereco.pessoa = pessoa
endereco.save()

#models telefone

tel1= Telefone(tipo= 1, numero = '9988-8899')
tel2= Telefone(tipo= 2, numero = '2626-2525')

tel1.pessoa = pessoa
tel2.pessoa = pessoa

tel1.save()
tel2.save()

Pessoa.objects.all()
Endereco.objects.all()
Telefone.objects.all()

pessoa_consultada = Pessoa.objects.filter(codigo = 2) .first()

pessoa_consultada.endereco = Endereco.objects.filter(pessoa = pessoa_consultada).first()

telefones = Telefone.objects.filter(pessoa = pessoa_consultada)

pessoa_consultada.telefones = telefones

print('-------------------')
print(pessoa_consultada)
print(pessoa_consultada.endereco)
print(pessoa_consultada.telefones)