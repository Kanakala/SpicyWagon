# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant', '0015_auto_20170203_0314'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='City_Code',
            field=models.CharField(default='HYB', max_length=6),
            preserve_default=False,
        ),
    ]
