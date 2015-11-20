# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Packages',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=256, verbose_name=b'name')),
            ],
        ),
        migrations.CreateModel(
            name='Repositories',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=256, verbose_name=b'name')),
                ('url', models.CharField(max_length=1024, verbose_name=b'URL')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('username', models.Field(max_length=100, verbose_name=b'username')),
                ('fullname', models.CharField(max_length=100, verbose_name=b'fullname')),
                ('email', models.CharField(max_length=256, verbose_name=b'email')),
                ('packages', models.ManyToManyField(to='api.Packages', verbose_name=b'packages')),
                ('repositories', models.ManyToManyField(to='api.Repositories', verbose_name=b'repositories')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
    ]
