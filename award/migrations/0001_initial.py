# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-03 19:55
from __future__ import unicode_literals

import award.validators
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
            name='EducationAward',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=150, null=True, validators=[award.validators.validate_eduaward_desc])),
                ('awardAmount', models.FloatField(max_length=5, null=True, validators=[award.validators.validate_award_amt])),
                ('awardRecipient', models.CharField(blank=True, max_length=60, null=True)),
                ('awardType', models.CharField(blank=True, choices=[(b'Internal', b'Internal'), (b'External', b'External')], max_length=8, null=True)),
                ('yearAwarded', models.IntegerField(blank=True, choices=[(2017, 2017), (2016, 2016), (2015, 2015), (2014, 2014), (2013, 2013), (2012, 2012), (2011, 2011), (2010, 2010), (2009, 2009), (2008, 2008), (2007, 2007), (2006, 2006), (2005, 2005), (2004, 2004), (2003, 2003), (2002, 2002), (2001, 2001), (2000, 2000), (1999, 1999), (1998, 1998), (1997, 1997), (1996, 1996), (1995, 1995), (1994, 1994), (1993, 1993), (1992, 1992), (1991, 1991), (1990, 1990), (1989, 1989), (1988, 1988), (1987, 1987), (1986, 1986), (1985, 1985), (1984, 1984), (1983, 1983), (1982, 1982), (1981, 1981), (1980, 1980)], max_length=4, null=True)),
                ('awardedMember', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='add_member.Person')),
            ],
        ),
        migrations.CreateModel(
            name='PDAward',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('awardName', models.CharField(max_length=50)),
                ('awardCost', models.FloatField(validators=[award.validators.validate_award_amt])),
                ('startDate', models.DateField(default=datetime.date(2017, 4, 3))),
                ('endDate', models.DateField(default=datetime.date(2017, 4, 3))),
                ('memberAwarded', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='add_member.Person')),
            ],
        ),
    ]
