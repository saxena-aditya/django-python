# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-25 11:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0002_auto_20170425_1138'),
    ]

    operations = [
        migrations.RenameField(
            model_name='options',
            old_name='question_id',
            new_name='question',
        ),
    ]
