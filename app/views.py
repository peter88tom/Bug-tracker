# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage(request):
	return render(request, 'index.html')

def new_bug(request):
	return render(request, 'new-bug.html')