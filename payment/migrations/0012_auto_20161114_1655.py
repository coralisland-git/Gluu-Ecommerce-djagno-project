# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-14 16:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0011_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='amount',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='payment',
            name='credits_used',
            field=models.FloatField(default=0.0),
        ),
    ]