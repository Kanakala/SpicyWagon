# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant', '0008_auto_20170123_2143'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='Image_Path',
            new_name='image_path',
        ),
    ]
