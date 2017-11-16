# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models


class User(models.Model):
    uname = models.CharField(max_length=70, primary_key=True)
    pwd = models.CharField(max_length=70)
    role = models.CharField(max_length=70)


class Participant(models.Model):
    uname = models.ForeignKey('User')
    challenge_id = models.CharField(max_length=20)
    score = models.IntegerField()
    total_score = models.IntegerField()

    class Meta:
        unique_together = (("uname", "challenge_id"),)


class Reviewer (models.Model):
    uname = models.ForeignKey('User')
    challenge_id = models.CharField(max_length=20)
    reviewed_uname = models.ForeignKey('User', related_name="reviewed_user")
    assigned_score = models.IntegerField()

    class Meta:
        unique_together = ("uname", "challenge_id", "reviewed_uname")
