from django import forms

class CreateNewBug(forms.Form):
	description  = forms.CharField(widget=forms.Textarea, required=True)
	project      = forms.IntegerField(required=True)