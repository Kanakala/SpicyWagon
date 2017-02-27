# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant', '0006_dish_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('Count', models.IntegerField()),
                ('Dish_Price', models.CharField(max_length=4)),
                ('Total_Amount', models.CharField(max_length=5)),
                ('Confirmed', models.BooleanField(default=False)),
                ('Dish', models.ForeignKey(to='Restaurant.Dish')),
            ],
        ),
        migrations.CreateModel(
            name='Total_Orders',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('Dish', models.CharField(max_length=30)),
                ('Dish_Price', models.CharField(max_length=4)),
                ('Total_Amount', models.CharField(max_length=5)),
                ('Order', models.ForeignKey(to='Customer.Order')),
            ],
        ),
    ]
