# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-11 14:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pintuan',
            name='name',
            field=models.CharField(default='PinTuan', max_length=200),
        ),
    ]
