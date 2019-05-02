from django import forms

class SearchForm(forms.Form):
	search = forms.CharField(label='Your name', max_length=100)
	choices = (('oldest', 'Mais Antigo'),('newest', 'Mais Novo'),)
	field = forms.ChoiceField(choices=choices)
    