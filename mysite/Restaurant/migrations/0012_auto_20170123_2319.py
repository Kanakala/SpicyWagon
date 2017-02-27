# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant', '0011_auto_20170123_2317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='image_path',
            field=models.CharField(null=True, blank=True, max_length=200),
        ),
    ]
