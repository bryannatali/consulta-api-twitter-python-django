from django import forms

class SearchForm(forms.Form):
	search = forms.CharField(label='Your name', max_length=100)