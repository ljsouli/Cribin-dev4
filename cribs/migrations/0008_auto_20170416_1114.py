# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-16 11:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cribs', '0007_auto_20170416_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cribimage',
            name='image',
            field=models.ImageField(blank=True, upload_to='cribs/static/cribs_pictures/'),
        ),
        migrations.AlterField(
            model_name='roomimage',
            name='image',
            field=models.ImageField(blank=True, upload_to='cribs/static/room_pictures/'),
        ),
    ]
