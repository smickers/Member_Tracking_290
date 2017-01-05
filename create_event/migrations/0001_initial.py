# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-05 21:22
from __future__ import unicode_literals

import create_event.validators
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('add_member', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, validators=[create_event.validators.validate_name])),
                ('description', models.CharField(blank=True, max_length=50, null=True, validators=[create_event.validators.validate_desc])),
                ('date', models.DateField(default=datetime.date.today)),
                ('location', models.CharField(max_length=25, validators=[create_event.validators.validate_location])),
                ('members', models.ManyToManyField(blank=True, related_name='event_members', to='add_member.Person')),
            ],
        ),
    ]
