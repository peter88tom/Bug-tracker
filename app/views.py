# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Project, Bug

# Create your views here.
def homepage(request):
	return render(request, 'index.html')

def new_bug(request):
	""" Handle form submission for creating new project bug """
	if request.method == "POST":
		print "we are posting data"
	else:
	    # Get a list of projects
	    list_of_projects = Project.objects.all()

	    return render(request, 'new-bug.html', {"projects":list_of_projects})