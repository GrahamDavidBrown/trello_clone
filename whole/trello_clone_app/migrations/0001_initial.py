# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-31 15:01
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=250)),
                ('comment', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=250)),
                ('cards', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trello_clone_app.Card')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('name_first', models.CharField(max_length=20)),
                ('name_last', models.CharField(max_length=20)),
                ('boards', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trello_clone_app.Board')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='board',
            name='lists',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trello_clone_app.List'),
        ),
    ]
