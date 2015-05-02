# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag_number', models.IntegerField(unique=True)),
                ('ident', models.CharField(unique=True, max_length=128)),
                ('name', models.CharField(max_length=128)),
                ('Aelement', models.CharField(max_length=2)),
                ('Belement', models.CharField(max_length=2)),
                ('Celement', models.CharField(max_length=2)),
                ('valenceNumber', models.IntegerField()),
                ('structure', models.CharField(max_length=4)),
                ('magneticMoment', models.DecimalField(null=True, max_digits=20, decimal_places=10, blank=True)),
                ('latticeConstant', models.DecimalField(null=True, max_digits=20, decimal_places=10, blank=True)),
                ('formationEnergy', models.DecimalField(null=True, max_digits=20, decimal_places=10, blank=True)),
                ('polarization', models.DecimalField(null=True, max_digits=20, decimal_places=10, blank=True)),
                ('stable', models.NullBooleanField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
