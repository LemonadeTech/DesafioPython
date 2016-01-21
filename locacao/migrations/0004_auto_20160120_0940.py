# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-20 11:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('locacao', '0003_clientes_veiculos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Devolucao',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quilometragem_inicial', models.IntegerField()),
                ('data_locacao', models.DateField()),
                ('data_devolucao', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='clientes',
            name='email_cliente',
            field=models.EmailField(max_length=254),
        ),
        migrations.AddField(
            model_name='devolucao',
            name='id_cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locacao.Clientes'),
        ),
        migrations.AddField(
            model_name='devolucao',
            name='id_veiculos',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locacao.Veiculos'),
        ),
    ]