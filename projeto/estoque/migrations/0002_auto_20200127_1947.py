# Generated by Django 2.2.8 on 2020-01-27 21:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EstoqueEntrada',
            fields=[
            ],
            options={
                'verbose_name': 'estoque_entrada',
                'verbose_name_plural': 'estoque_entrada',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('estoque.estoque',),
        ),
        migrations.CreateModel(
            name='EstoqueSaida',
            fields=[
            ],
            options={
                'verbose_name': 'estoque_saida',
                'verbose_name_plural': 'estoque_saida',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('estoque.estoque',),
        ),
        migrations.AlterField(
            model_name='estoqueitens',
            name='estoque',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='estoques', to='estoque.Estoque'),
        ),
    ]
