# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-16 20:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('challenge_id', models.CharField(max_length=20)),
                ('score', models.IntegerField()),
                ('total_score', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Reviewer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('challenge_id', models.CharField(max_length=20)),
                ('assigned_score', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('uname', models.CharField(max_length=70, primary_key=True, serialize=False)),
                ('pwd', models.CharField(max_length=70)),
                ('role', models.CharField(max_length=70)),
            ],
        ),
        migrations.AddField(
            model_name='reviewer',
            name='reviewed_uname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviewed_user', to='crt.User'),
        ),
        migrations.AddField(
            model_name='reviewer',
            name='uname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crt.User'),
        ),
        migrations.AddField(
            model_name='participant',
            name='uname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crt.User'),
        ),
        migrations.AlterUniqueTogether(
            name='reviewer',
            unique_together=set([('uname', 'challenge_id', 'reviewed_uname')]),
        ),
        migrations.AlterUniqueTogether(
            name='participant',
            unique_together=set([('uname', 'challenge_id')]),
        ),
    ]