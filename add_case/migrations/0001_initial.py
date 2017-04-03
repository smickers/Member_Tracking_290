# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-30 19:29
from __future__ import unicode_literals

import add_case.validators
import datetime
from django.db import migrations, models
import django.db.models.deletion


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
                ('campus', models.CharField(choices=[(b'Regina', b'Regina'), (b'PA', b'Prince Albert'), (b'Saskatoon', b'Saskatoon'), (b'MJ', b'Moose Jaw')], default='Saskatoon', max_length=25, validators=[add_case.validators.validate_location])),
                ('satellite', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('school', models.CharField(choices=[(b'School of Business', b'School of Business'), (b'School of Mining, Energy and Manufacturing', b'School of Mining, Energy and Manufacturing'), (b'Other', b'Other'), (b'School of Natural Resources and Built Environment', b'School of Natural Resources and Built Environment'), (b'School of Nursing', b'School of Nursing'), (b'School of Transportation', b'School of Transportation'), (b'School of Construction', b'School of Construction'), (b'School of Health Sciences', b'School of Health Sciences'), (b'School of Information and Communications Technology', b'School of Information and Communications Technology'), (b'School of Human Services and Community Safety', b'School of Human Services and Community Safety')], max_length=255)),
                ('department', models.CharField(blank=True, choices=[(b'Student Development', b'Student Development'), (b'ILDC', b'ILDC'), (b'Learning Technologies', b'Learning Technologies'), (b'Learning Services', b'Learning Services'), (b'PLAR', b'PLAR'), (b'Simulation Lab', b'Simulation Lab'), (b'Library', b'Library'), (b'Fitness Centre', b'Fitness Centre')], default=None, max_length=255, null=True)),
                ('caseType', models.IntegerField(choices=[(7, b'GRIEVANCES - INDIVIDUAL'), (6, b'GRIEVANCES - GROUP'), (5, b'GRIEVANCES - POLICY'), (4, b'GRIEVANCES - CLASSIFICATION'), (3, b'GRIEVANCES - COMPLAINTS'), (2, b'DISABILITY CLAIMS'), (1, b'ARBITRATION'), (0, b'COMPLAINT')])),
                ('status', models.CharField(choices=[(b'OPEN', b'OPEN'), (b'CLOSED', b'CLOSED'), (b'PENDING', b'PENDING'), (b"ACTION REQ'D - MGMT", b"ACTION REQ'D - MGMT"), (b"ACTION REQ'D SPFA", b"ACTION REQ'D SPFA")], default='OPEN', max_length=15)),
                ('additionalNonMembers', models.TextField(blank=True, null=True)),
                ('docs', models.TextField(blank=True, null=True)),
                ('date', models.DateField(blank=True, default=datetime.date.today, null=True, validators=[add_case.validators.validate_date])),
                ('additionalMembers', models.ManyToManyField(blank=True, to='add_member.Person')),
                ('complainant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='case_complainant', to='add_member.Person')),
            ],
        ),
        migrations.CreateModel(
            name='CaseFiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_uploaded', models.DateTimeField(auto_now=True, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='case/')),
                ('description', models.CharField(blank=True, max_length=50, null=True)),
                ('case', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='add_case.Case')),
            ],
        ),
        migrations.CreateModel(
            name='CaseMembers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caseNum', models.CharField(max_length=9)),
                ('memberNum', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CasePrograms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CaseSatellite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='case',
            name='program',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='add_case.CasePrograms'),
        ),
    ]
