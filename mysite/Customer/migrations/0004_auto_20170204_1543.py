# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0003_pnrsearch_search_trainsearch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainsearch',
            name='Boarding',
            field=models.CharField(blank=True, null=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='trainsearch',
            name='Date',
            field=models.CharField(max_length=30),
        ),
    ]
