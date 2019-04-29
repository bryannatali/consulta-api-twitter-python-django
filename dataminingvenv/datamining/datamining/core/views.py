from django.shortcuts import render
from django.http import HttpResponse
from requests_oauthlib import OAuth1Session
import requests.utils
import json
from .api_search import TwitterUtil
from .forms import SearchForm
from datamining.core.models import SentimentAnalysis
import re

def index(request):
	form = SearchForm()
	return render(request, 'index.html', {'form': form})

def procurar(request):

	if request.method == 'POST':
		form = SearchForm(request.POST or None)
		if form.is_valid():
			search = form.cleaned_data['search']

			client = TwitterUtil()

			tweets = client.get_tweets("ifsc "+ search, 1000)

			list_tweet = []

			for tweet in range(0, len(tweets)):
				aux = tweets[tweet]['user']['location']

				if (re.search('brasil', aux, re.IGNORECASE) ):
					list_tweet.append(tweets[tweet])
					
			quantity = len(list_tweet)

			return render(request, 'procurar.html', {'tweets': list_tweet, 'quantity': quantity} )
	else:
		form = SearchForm()
		return render(request, 'index.html', {'form': form})
	


def graficos(request):

	return render(request, 'graficos.html')