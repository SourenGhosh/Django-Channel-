# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2021-10-07 19:36
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
            name='ButtonTracker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fat_count', models.IntegerField(blank=True, default=0, null=True)),
                ('stupid_count', models.IntegerField(blank=True, default=0, null=True)),
                ('dumb_count', models.IntegerField(blank=True, default=0, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
