# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='state_province',
            field=models.CharField(help_text=b'State/Province', max_length=25, blank=True),
        ),
    ]
