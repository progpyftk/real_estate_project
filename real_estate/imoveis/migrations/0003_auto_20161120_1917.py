# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-11-20 21:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imoveis', '0002_auto_20161120_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anuncio',
            name='image_principal',
            field=models.ImageField(upload_to='anuncios/%Y/%m/%d'),
        ),
    ]
