from django import forms

class CadastroForm(forms.Form):

    nome = forms.CharField(max_length=100, label='Informe o nome ',required=False)
    email = forms.CharField(max_length=100, label='Informe o email ', required=False)

    cidade = forms.CharField(max_length=100, label='Informe a cidade ',required=False)

    bairro = forms.CharField(max_length=100, label='Informe a bairro ',required=False)

    logradouro = forms.CharField(max_length=100, label='Informe a rua ', required=False)

    uf = forms.CharField(max_length=100, label='Informe o estado ', required=False)

    cep = forms.CharField(max_length=100, label='Informe a cep ',required=False)

    complemento = forms.CharField(max_length=100, label='Informe o complemento ', required=False)


    numero1 = forms.CharField(max_length=100, label='Informe o telefone residencial ', required=False)
    numero2 = forms.CharField(max_length=100, label='Informe o telefone celular ', required=False)

    pass
