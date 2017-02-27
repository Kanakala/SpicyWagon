# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant', '0007_restaurant_image_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='Image_Path',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
