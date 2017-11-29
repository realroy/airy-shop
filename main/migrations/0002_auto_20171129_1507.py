# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-29 08:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
            ],
            options={
                'verbose_name': 'Manager',
                'verbose_name_plural': 'Manager',
                'proxy': True,
                'indexes': [],
            },
            bases=('main.transaction',),
        ),
        migrations.AddField(
            model_name='transaction',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='product',
            name='pic',
            field=models.ImageField(default='../static/imgs/empty.png', max_length=500, upload_to='imgs/'),
        ),
    ]