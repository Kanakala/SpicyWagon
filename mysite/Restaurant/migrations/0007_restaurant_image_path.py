# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant', '0006_dish_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='Image_Path',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
