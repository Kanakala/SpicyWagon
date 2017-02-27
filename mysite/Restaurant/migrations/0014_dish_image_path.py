# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant', '0013_auto_20170202_1832'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='image_path',
            field=models.CharField(null=True, max_length=200, blank=True),
        ),
    ]
