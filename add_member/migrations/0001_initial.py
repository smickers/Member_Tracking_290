# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-01 15:14
from __future__ import unicode_literals

import add_member.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('memberID', models.IntegerField(validators=[add_member.validators.validate_ninedigits])),
                ('firstName', models.CharField(max_length=30, validators=[add_member.validators.validate_rightstringlen30])),
                ('middleName', models.CharField(max_length=30, validators=[add_member.validators.validate_rightstringlen30])),
                ('lastName', models.CharField(max_length=30, validators=[add_member.validators.validate_rightstringlen30])),
                ('socNum', models.IntegerField(validators=[add_member.validators.validate_ninedigits])),
                ('city', models.CharField(max_length=20, validators=[add_member.validators.validate_rightstringlen20])),
                ('mailAddress', models.CharField(max_length=50, validators=[add_member.validators.validate_rightstringlen50])),
                ('mailAddress2', models.CharField(blank=True, max_length=50, null=True, validators=[add_member.validators.validate_rightstringlen50])),
                ('pCode', models.CharField(max_length=7, validators=[add_member.validators.validate_pCode])),
                ('bDay', models.DateField()),
                ('gender', models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female'), ('UNDEFINED', 'Undefined')], max_length=10)),
                ('hPhone', models.CharField(blank=True, max_length=13, null=True, validators=[add_member.validators.validate_numbers])),
                ('cPhone', models.CharField(blank=True, max_length=13, null=True, validators=[add_member.validators.validate_numbers])),
                ('hEmail', models.EmailField(max_length=254)),
                ('campus', models.CharField(choices=[('SASKATOON', 'SASKATOON'), ('REGINA', 'REGINA'), ('MOOSEJAW', 'MOOSE JAW'), ('PA', 'PRINCE ALBERT')], max_length=20)),
                ('jobType', models.CharField(choices=[('FTO', 'Full-time ongoing'), ('FTED', 'Full-time end dated'), ('PTO', 'Part-time ongoing'), ('PTED', 'Part-time end dated')], max_length=30)),
                ('committee', models.CharField(max_length=30, validators=[add_member.validators.validate_rightstringlen30])),
                ('memberImage', models.CharField(blank=True, max_length=30, null=True)),
                ('programChoice', models.CharField(max_length=30, null=True, validators=[add_member.validators.validate_rightstringlen30])),
                ('membershipStatus', models.CharField(choices=[('RESOURCE', 'RESOURCE'), ('COMCHAIR', 'COMMITTEE CHAIR'), ('RECORDER', 'RECORDER')], max_length=30, null=True)),
                ('hireDate', models.DateField(null=True)),
            ],
        ),
    ]
