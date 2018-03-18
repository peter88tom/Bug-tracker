# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Project model.
class Project(models.Model):
	project_name = models.CharField(max_length=255, null=False, blank=False)



# Bug model
class Bug(models.Model):
	description = models.TextField()
	project = models.ForeignKey(Project, on_delete=models.CASCADE)
	date_added = models.DateField(null=False, blank=False)