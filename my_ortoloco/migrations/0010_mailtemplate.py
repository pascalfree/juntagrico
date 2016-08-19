# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-08-19 10:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_ortoloco', '0009_auto_20160815_1041'),
    ]

    operations = [
        migrations.CreateModel(
            name='MailTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name=b'Name')),
                ('template', models.TextField(default=b'', max_length=1000, verbose_name=b'Template')),
                ('code', models.TextField(default=b'', max_length=1000, verbose_name=b'Code')),
            ],
            options={
                'verbose_name': 'MailTemplate',
                'verbose_name_plural': 'MailTemplates',
            },
        ),
    ]
