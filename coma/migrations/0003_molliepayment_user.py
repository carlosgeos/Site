# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-28 18:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency('members.Member'),
        ('coma', '0002_molliepayment'),
    ]

    operations = [
        migrations.AddField(
            model_name='molliepayment',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='members.Member'),
            preserve_default=False,
        ),
    ]