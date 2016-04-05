# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icinema', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Films',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_film', models.IntegerField()),
                ('title', models.TextField(null=True, blank=True)),
                ('classification', models.TextField(null=True, blank=True)),
                ('advisory_age', models.IntegerField()),
                ('sipnosis', models.TextField(null=True, blank=True)),
                ('duration', models.IntegerField()),
                ('autors', models.TextField(null=True, blank=True)),
                ('directors', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Performances',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_performance', models.IntegerField()),
                ('time', models.IntegerField(null=True, blank=True)),
                ('avaiable', models.TextField(null=True, blank=True)),
                ('type', models.TextField(null=True, blank=True)),
                ('date', models.DateField()),
            ],
        ),
    ]
