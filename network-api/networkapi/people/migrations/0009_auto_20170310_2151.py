# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-10 21:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0008_auto_20170309_2326'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='teams',
        ),
        migrations.DeleteModel(
            name='Team',
        ),
    ]
