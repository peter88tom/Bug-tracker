# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Project, Bug

# Register your models here.
admin.site.register(Project)
admin.site.register(Bug)