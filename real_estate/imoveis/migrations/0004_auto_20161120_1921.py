# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-11-20 21:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imoveis', '0003_auto_20161120_1917'),
    ]

    operations = [
        migrations.RenameField(
            model_name='anuncio',
            old_name='image_principal',
            new_name='imagem_principal',
        ),
    ]