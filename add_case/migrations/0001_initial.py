# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-01-04 19:41
from __future__ import unicode_literals

import add_case.validators
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('add_member', '0001_initial'),
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
                ('department', models.CharField(max_length=255, null=True)),
                ('caseType', models.CharField(max_length=50, validators=[add_case.validators.validate_case_type])),
                ('status', models.CharField(blank=True, default='OPEN', max_length=50, validators=[add_case.validators.validate_status])),
                ('additionalNonMembers', models.TextField(blank=True, null=True)),
                ('docs', models.TextField(blank=True, null=True)),
                ('logs', models.TextField(blank=True, null=True)),
                ('date', models.DateField(blank=True, default=datetime.date.today, null=True, validators=[add_case.validators.validate_date])),
                ('additionalMembers', models.ManyToManyField(blank=True, default=None, null=True, to='add_member.Person')),
            ],
        ),
        migrations.CreateModel(
            name='CaseMembers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caseNum', models.CharField(max_length=9)),
                ('memberNum', models.TextField()),
                ('caseMember', models.CharField(max_length=18, null='true', unique='true')),
            ],
        ),
    ]
