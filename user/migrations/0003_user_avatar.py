# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-27 15:27
from __future__ import unicode_literals

from django.db import migrations, models
import user.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_hasshop'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to=user.models.user_upload_to),
        ),
    ]
