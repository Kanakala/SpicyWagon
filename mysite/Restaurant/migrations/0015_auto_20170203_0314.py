# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant', '0014_dish_image_path'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='no',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='submenu',
            name='no',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
