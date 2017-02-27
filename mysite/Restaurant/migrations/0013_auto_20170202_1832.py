# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Restaurant', '0012_auto_20170123_2319'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubMenu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('Sub_Menu', models.CharField(max_length=30)),
                ('Menu', models.ForeignKey(to='Restaurant.Menu', related_name='submenu_menu')),
                ('Restaurant', models.ForeignKey(to='Restaurant.Restaurant', related_name='submenu_restaurant')),
                ('user', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='dish',
            name='Sub_Menu',
            field=models.ForeignKey(null=True, to='Restaurant.SubMenu', related_name='dish_submenu', blank=True),
        ),
    ]
