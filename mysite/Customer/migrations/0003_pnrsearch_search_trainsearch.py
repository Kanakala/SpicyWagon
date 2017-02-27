# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0002_order_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='PnrSearch',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('Pnr', models.CharField(max_length=10)),
                ('TimeStamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('Pnr', models.CharField(max_length=10, blank=True, null=True)),
                ('TrainDetails', models.CharField(max_length=30, blank=True, null=True)),
                ('Date', models.CharField(max_length=20, blank=True, null=True)),
                ('Boarding', models.CharField(max_length=20, blank=True, null=True)),
                ('TimeStamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='TrainSearch',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('TrainDetails', models.CharField(max_length=30)),
                ('Date', models.CharField(max_length=20)),
                ('Boarding', models.CharField(max_length=20, blank=True, null=True)),
                ('TimeStamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
