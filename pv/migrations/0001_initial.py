# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-26 21:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import pv.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PV',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ressource', models.FileField(upload_to=pv.models.determine_name)),
                ('meeting_date', models.DateField(verbose_name='Date de la réunion')),
                ('upload_date', models.DateField(default=django.utils.timezone.now, verbose_name="Date de l'upload")),
                ('reunion_type', models.CharField(blank=True, choices=[('N', 'Réunion normale'), ('B', 'Réunion de bureau'), ('AG', 'Assemblée générale élective')], default='N', max_length=2, verbose_name='Type de réunion')),
                ('year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.AcademicYear', verbose_name='Année de comité du pv')),
            ],
            options={
                'ordering': ['-meeting_date'],
            },
        ),
    ]
