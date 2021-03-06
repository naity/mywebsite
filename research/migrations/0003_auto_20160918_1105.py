# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-18 18:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0002_auto_20160917_2328'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='figure',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='publications/figures'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='publication',
            name='pdf',
            field=models.FileField(upload_to='publications/pdfs'),
        ),
    ]
