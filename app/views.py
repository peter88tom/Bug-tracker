# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Project, Bug
from .forms import CreateNewBug

# Create your views here.
def homepage(request):
	return render(request, 'index.html')

def new_bug(request):
	
	""" Get list of projects to show on selection """
	list_of_projects = Project.objects.all()

	""" Handle form submission for creating new project bug """
	if request.method == "POST":
		form = CreateNewBug(request.POST)
		if form.is_valid():
			""" Get project instance """
			project = Project.objects.get(pk=request.POST.get('project'))
			date_added = form.cleaned_data['date_added']
			description = form.cleaned_data['description']

			""" save bug """
			savebug = Bug(description=description,project=project,date_added=date_added)
			savebug.save()

			
			return render(request, 'new-bug.html', {"form":form, "projects":list_of_projects} )

		""" Handle invalid form submission """
		return render(request, 'new-bug.html', {"form":form, "projects":list_of_projects})

	""" Handle other type of requests such as GET """
	form = CreateNewBug()
	return render(request, 'new-bug.html', {"form":form, "projects":list_of_projects})