# -*- coding: utf-8 -*-
# Generated by Django 1.11rc1 on 2017-07-26 23:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homeslide',
            name='image',
            field=models.ImageField(default='', upload_to='home/%Y-%m-%d/'),
        ),
    ]