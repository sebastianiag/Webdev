# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0003_auto_20150412_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='education_level',
            field=models.CharField(default=b' ', max_length=2, choices=[(b'PE', b'Primary Education'), (b'SE', b'High School'), (b'CO', b'College'), (b' ', b' ')]),
        ),
    ]
