# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-16 22:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dish',
            name='Menu_Name',
        ),
        migrations.RemoveField(
            model_name='dish',
            name='Restaurant_Name',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='Restaurant_Name',
        ),
    ]
