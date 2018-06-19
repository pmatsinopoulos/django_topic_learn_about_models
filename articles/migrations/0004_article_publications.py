# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-19 05:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_publication'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='publications',
            field=models.ManyToManyField(to='articles.Publication'),
        ),
    ]