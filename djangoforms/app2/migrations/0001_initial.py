# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-31 03:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app1', '0004_auto_20180331_0333'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyProduct',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app1.Product')),
                ('color', models.CharField(max_length=30)),
            ],
            bases=('app1.product',),
        ),
        migrations.CreateModel(
            name='ProductProxy',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('app1.product',),
        ),
    ]
