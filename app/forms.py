from django import forms

class CreateNewBug(forms.Form):
	description  = forms.TextField(required=True)
	project      = forms.IntegerField(required=True)
	date_added   = forms.DateField(required = True)