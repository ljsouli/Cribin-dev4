# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-13 12:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cribs', '0004_auto_20170412_1956'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllCribEquipments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='AllHobbies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='AllLanguages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('lang', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='AllRoomEquipments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='AllStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='CribEquipments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crib_equipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cribs.AllCribEquipments')),
                ('crib_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cribs.Crib')),
            ],
        ),
        migrations.CreateModel(
            name='CribImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.TextField(blank=True)),
                ('crib', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cribs.Crib')),
            ],
        ),
        migrations.CreateModel(
            name='GuestHobbies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guest_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cribs.Guest')),
                ('hobby', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cribs.AllHobbies')),
            ],
        ),
        migrations.CreateModel(
            name='GuestLanguages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guest_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cribs.Guest')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cribs.AllStatus')),
            ],
        ),
        migrations.CreateModel(
            name='GuestStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guest_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cribs.Guest')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cribs.AllStatus')),
            ],
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('last_name', models.CharField(max_length=50)),
                ('fist_name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=254)),
                ('image', models.ImageField(upload_to=b'')),
                ('gender', models.CharField(max_length=1)),
                ('birth_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='HostHobbies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hobby', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cribs.AllHobbies')),
                ('host_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cribs.Host')),
            ],
        ),
        migrations.CreateModel(
            name='HostLanguages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cribs.Host')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cribs.AllStatus')),
            ],
        ),
        migrations.CreateModel(
            name='HostStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cribs.Host')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cribs.AllStatus')),
            ],
        ),
        migrations.CreateModel(
            name='Rents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('begin_date', models.DateField()),
                ('end_date', models.DateField()),
                ('price', models.PositiveIntegerField(default=1)),
                ('transaction_date', models.DateField()),
                ('crib_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cribs.Crib')),
                ('guest_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cribs.Guest')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True)),
                ('price', models.PositiveIntegerField(default=1)),
                ('avalaible_from', models.DateField()),
                ('avalaible_to', models.DateField()),
                ('avalaible', models.BooleanField()),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cribs.Host')),
            ],
        ),
        migrations.CreateModel(
            name='RoomEquipments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_equipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cribs.AllRoomEquipments')),
                ('room_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cribs.Room')),
            ],
        ),
        migrations.CreateModel(
            name='RoomImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.TextField(blank=True)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cribs.Room')),
            ],
        ),
        migrations.AddField(
            model_name='rents',
            name='room_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cribs.Room'),
        ),
        migrations.AddField(
            model_name='crib',
            name='host',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cribs.Host'),
            preserve_default=False,
        ),
    ]