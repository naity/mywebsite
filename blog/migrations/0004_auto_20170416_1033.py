# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-16 17:33
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170416_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='abstract',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
