# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-26 10:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merchandise', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='merchandise',
            name='price',
            field=models.DecimalField(decimal_places=0, max_digits=6),
        ),
    ]
