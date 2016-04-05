# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cinema',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_cinema', models.IntegerField()),
                ('name', models.TextField(null=True, blank=True)),
                ('cinema_url', models.TextField(null=True, blank=True)),
                ('adress', models.TextField(null=True, blank=True)),
                ('postcode', models.IntegerField()),
                ('telephone', models.IntegerField()),
            ],
        ),
    ]
