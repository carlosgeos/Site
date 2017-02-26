# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-11-24 13:48
from __future__ import unicode_literals
from members.models import Member
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0006_remove_20161124_1448'),
    ]

    def gen_uuid(apps, schema_editor):
        for row in Member.objects.all():
            row.card_id = uuid.uuid4()
            row.save()

    operations = [
        migrations.AddField(
            model_name='member',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),

        migrations.AddField(
            model_name='member',
            name='card_id',
            field=models.UUIDField(default=uuid.uuid4),
        ),

        migrations.RunPython(gen_uuid),

        migrations.AlterField(
            model_name='member',
            name='card_id',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
    ]
