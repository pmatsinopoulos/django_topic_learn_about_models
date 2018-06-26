# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-26 19:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0001_create_questions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_text', models.TextField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizzes.Question')),
            ],
            options={
                'db_table': 'quizzes_answers',
            },
        ),
        migrations.AlterOrderWithRespectTo(
            name='answer',
            order_with_respect_to='question',
        ),
    ]
