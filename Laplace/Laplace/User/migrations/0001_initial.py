# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('addressLine1', models.CharField(max_length=32, blank=True)),
                ('addressLine2', models.CharField(max_length=32, blank=True)),
                ('city', models.CharField(max_length=25, blank=True)),
                ('state_province', models.CharField(max_length=25, blank=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Colleges',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, blank=True)),
                ('highest_degree', models.CharField(max_length=50, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('course', models.CharField(max_length=50, blank=True)),
                ('offered', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Interests',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('interest', models.CharField(max_length=25, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Schools',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, blank=True)),
                ('highest_grade', models.CharField(max_length=50, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('email', models.EmailField(unique=True, max_length=254)),
                ('username', models.CharField(unique=True, max_length=25)),
                ('first_name', models.CharField(max_length=25, blank=True)),
                ('last_name', models.CharField(max_length=25, blank=True)),
                ('description', models.CharField(max_length=200, blank=True)),
                ('birthdate', models.DateField(blank=True)),
                ('is_tutor', models.BooleanField(default=False)),
                ('joined_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('education_level', models.CharField(blank=True, max_length=2, choices=[(b'PE', b'Primary Education'), (b'SE', b'High School'), (b'CO', b'College')])),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='schools',
            name='user',
            field=models.ForeignKey(related_name='schools', to='User.User'),
        ),
        migrations.AddField(
            model_name='interests',
            name='user',
            field=models.ForeignKey(related_name='interests', to='User.User'),
        ),
        migrations.AddField(
            model_name='courses',
            name='user',
            field=models.ForeignKey(related_name='courses', to='User.User'),
        ),
        migrations.AddField(
            model_name='colleges',
            name='user',
            field=models.ForeignKey(related_name='colleges', to='User.User'),
        ),
        migrations.AddField(
            model_name='address',
            name='user',
            field=models.ForeignKey(related_name='address', to='User.User'),
        ),
    ]
