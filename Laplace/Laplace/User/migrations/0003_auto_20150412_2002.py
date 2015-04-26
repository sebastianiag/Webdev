# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_auto_20150412_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birthdate',
            field=models.CharField(max_length=10, blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='education_level',
            field=models.CharField(blank=True, max_length=2, choices=[(b'PE', b'Primary Education'), (b'SE', b'High School'), (b'CO', b'College'), (b'', b'')]),
        ),
    ]
