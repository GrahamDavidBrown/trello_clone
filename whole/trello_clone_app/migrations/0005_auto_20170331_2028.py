# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-31 20:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trello_clone_app', '0004_auto_20170331_2020'),
    ]

    operations = [
        migrations.RenameField(
            model_name='card',
            old_name='cards',
            new_name='lists',
        ),
    ]