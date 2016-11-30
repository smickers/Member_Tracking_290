# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-27 20:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lead', models.IntegerField(max_length=9)),
                ('complainant', models.IntegerField(max_length=9)),
                ('campus', models.CharField(max_length=20)),
                ('school', models.CharField(max_length=255)),
                ('caseType', models.CharField(max_length=50)),
                ('status', models.CharField(blank=True, max_length=50)),
                ('additionalMembers', models.IntegerField(blank=True, max_length=9)),
                ('additionalNonMembers', models.TextField(blank=True)),
                ('docs', models.TextField(blank=True)),
                ('logs', models.TextField(blank=True)),
                ('date', models.DateField(blank=True)),
            ],
        ),
    ]