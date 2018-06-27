# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-27 16:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_article_publications'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024)),
                ('tagline', models.TextField()),
            ],
            options={
                'db_table': 'articles_blogs',
            },
        ),
    ]
