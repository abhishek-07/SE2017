# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-14 04:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20171013_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='Date_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 14, 4, 23, 8, 212709)),
        ),
        migrations.AlterField(
            model_name='attendance_session',
            name='Date_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 14, 4, 23, 8, 211751)),
        ),
        migrations.AlterField(
            model_name='logintable',
            name='Start_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 14, 4, 23, 8, 214311)),
        ),
    ]