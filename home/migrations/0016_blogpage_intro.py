# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-22 11:00
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_auto_20160422_0647'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='intro',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
    ]
