# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-07-24 19:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('pub_time', models.DateTimeField()),
                ('reading', models.IntegerField(default=0)),
                ('comments', models.IntegerField(default=0)),
                ('isDelete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'book',
            },
            managers=[
                ('manager1', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('gender', models.BooleanField()),
                ('introduce', models.CharField(max_length=50)),
                ('isDelete', models.BooleanField(default=False)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booktest.Book')),
            ],
            options={
                'db_table': 'hero',
            },
        ),
    ]
