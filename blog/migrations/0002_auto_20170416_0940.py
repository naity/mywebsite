# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-16 16:40
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articleimage',
            name='article',
        ),
        migrations.AlterField(
            model_name='article',
            name='text',
            field=tinymce.models.HTMLField(),
        ),
        migrations.DeleteModel(
            name='ArticleImage',
        ),
    ]
