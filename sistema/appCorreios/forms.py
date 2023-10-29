from django import forms

class CadastroForm(forms.Form):
    nome = forms.CharField(max_length=50, label='Informe o nome ')
    email = forms.CharField(max_length=100, label='Informe o email')

    cidade = forms.CharField(max_length=100, label='Informe a cidade')
    bairro = forms.CharField(max_length=100, label='Informeseu bairro')
    logradouro = forms.CharField(max_length=100, label='Informe a rua')
    uf = forms.CharField(max_length=100, label='Informe o estado')
    cep = forms.CharField(max_length=100, label='Informe  cep')
    complemento = forms.CharField(max_length=100, label='Informe o complemento')

    numero1= forms.CharField(max_length=100, label='Informe o telefone rsidencial ')
    numero2= forms.CharField(max_length=100, label='Informe o telefone celular ')


    pass