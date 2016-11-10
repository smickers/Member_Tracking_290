# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-07 15:41
from __future__ import unicode_literals

import add_case.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('add_case', '0002_auto_20161102_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='caseType',
            field=models.CharField(max_length=50, validators=[add_case.validators.validate_case_type]),
        ),
        migrations.AlterField(
            model_name='case',
            name='date',
            field=models.DateField(blank=True, null=True, validators=[add_case.validators.validate_date]),
        ),
        migrations.AlterField(
            model_name='case',
            name='status',
            field=models.CharField(blank=True, max_length=50, validators=[add_case.validators.validate_status]),
        ),
    ]
