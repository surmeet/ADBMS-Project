# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-12 14:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0010_auto_20160912_1955'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='attendance',
        ),
    ]
