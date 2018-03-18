# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Project model.
class Projects(models.Model):
	project_name = models.CharField(max_length=255, null=False, blank=False)


# Bug model
class Bugs(models.Model):
	description = models.TextField()
	project = models.ForeignKey(Projects, on_delete=models.CASCADE)
	date_added = models.DateField(null=False, blank=False)