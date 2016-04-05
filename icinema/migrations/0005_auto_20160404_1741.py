# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('icinema', '0004_auto_20160404_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='cinema',
            name='city',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='cinema',
            name='country',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='cinema',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='cinema',
            name='stateOrProvince',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='cinema',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
        ),
    ]
