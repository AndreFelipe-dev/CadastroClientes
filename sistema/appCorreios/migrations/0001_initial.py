# Generated by Django 3.2.22 on 2023-11-05 20:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'db_table': 'pessoa',
            },
        ),
        migrations.CreateModel(
            name='Telefone',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('numero', models.CharField(max_length=30)),
                ('tipo', models.IntegerField(choices=[(1, 'Res'), (2, 'Cel')])),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appCorreios.pessoa')),
            ],
            options={
                'db_table': 'telefone',
            },
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('cidade', models.CharField(max_length=100)),
                ('bairro', models.CharField(max_length=100)),
                ('logradouro', models.CharField(max_length=100)),
                ('uf', models.CharField(max_length=5)),
                ('cep', models.CharField(max_length=20)),
                ('complemento', models.CharField(max_length=100)),
                ('pessoa', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='appCorreios.pessoa')),
            ],
            options={
                'db_table': 'endereco',
            },
        ),
    ]
