# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-08 04:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logreg', '0003_auto_20160807_2054'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='desc',
            field=models.CharField(blank=True, max_length=140),
        ),
    ]
