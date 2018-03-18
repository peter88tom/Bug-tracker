# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Project, Bug
from .forms import CreateNewBug
from django.contrib import messages

# Create your views here.
def homepage(request):

	""" Get list of all bugs """
	bugs = Bug.objects.all()

	args = {"bugs":bugs}
	
	return render(request, 'index.html', args)

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

			msg = messages.success(request, 'saved successfuly')
			return redirect(new_bug)

		""" Handle invalid form submission """
		args = {"form":form, "projects":list_of_projects}
		return render(request, 'new-bug.html', args)

	""" Handle other type of requests such as GET """
	form = CreateNewBug()
	args = {"form":form, "projects":list_of_projects}
	return render(request, 'new-bug.html', args)