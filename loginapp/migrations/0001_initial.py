# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-14 09:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='login_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=250)),
                ('pass_word', models.CharField(max_length=250)),
            ],
        ),
    ]
