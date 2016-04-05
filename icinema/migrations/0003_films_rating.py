# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icinema', '0002_films_performances'),
    ]

    operations = [
        migrations.AddField(
            model_name='films',
            name='rating',
            field=models.PositiveSmallIntegerField(default=3, verbose_name=b'Rating (stars)', choices=[(1, b'one'), (2, b'two'), (3, b'three'), (4, b'four'), (5, b'five')]),
        ),
    ]
