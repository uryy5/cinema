# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icinema', '0005_auto_20160404_1741'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cinema',
            name='id_cinema',
        ),
        migrations.AlterField(
            model_name='cinema',
            name='cinema_url',
            field=models.URLField(null=True, blank=True),
        ),
    ]
