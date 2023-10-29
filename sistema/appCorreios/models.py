from django.db import models

class Pessoa(models.Model):

    class Meta:
        db_table = 'pessoa'

    codigo =models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, null=False)
    email = models.CharField(max_length=100, null=False, unique=True)

    def __str__(self):
        return '{}, {}, {}' . format(self.codigo, self.nome,self.email)

    def __repr__(self):
        return '{}, {}, {}'.format(self.codigo, self.nome, self.email)

pass

class Endereco(models.Model):

    class Meta:
        db_table = 'endereco'

    codigo = models.AutoField(primary_key=True)
    cidade = models.CharField(max_length=100, null=False)
    bairro = models.CharField(max_length=100, null=False)
    logradouro = models.CharField(max_length=100, null=False)
    uf = models.CharField(max_length=5, null=False)
    cep = models.CharField(max_length=20, null=False)
    complemento = models.CharField(max_length=100, null=False)

    pessoa = models.OneToOneField(Pessoa, on_delete = models.CASCADE, unique=True)

    def __str__(self):
        return '{}, {}, {}, {}, {}, {} ,{}' .format(self.codigo, self.cidade, self.bairro, self.logradouro, self.uf,
                                              self.cep, self.complemento)

    def __repr__(self):
        return '{}, {} , {}, {}, {} , {} ,{}' .format(self.codigo, self.cidade, self.bairro, self.logradouro, self.uf,
                                              self.cep, self.complemento)

    pass


class Telefone(models.Model):

    class Meta:
        db_table = 'telefone'

    class Tipo(models.IntegerChoices):

        RES = 1
        CEL = 2

    codigo = models.AutoField(primary_key=True)
    tipo = models.IntegerField(choices=Tipo.choices)
    numero = models.CharField(max_length=30, null=False)

    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE,)

    def __str__(self):

        return '{} , {} ,{}'.format(self.codigo, self.tipo, self.numero)

    def __repr__(self):

        return '{} , {}, {}' .format(self.codigo, self.tipo, self.numero)

    pass
