# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icinema', '0007_cinemareview'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cinemareview',
            old_name='restaurant',
            new_name='cinema',
        ),
    ]
