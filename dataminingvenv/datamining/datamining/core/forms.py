from django import forms

class SearchForm(forms.Form):
	search = forms.CharField(label='Your name', max_length=100)
	choices = (('newest', 'Mais Novo'),('oldest', 'Mais Antigo'),('morert', 'Mais Retwetado'), ('minusrt', 'Menos Retwetado'))
	field = forms.ChoiceField(choices=choices)
    