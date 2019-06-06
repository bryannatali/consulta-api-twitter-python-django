from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.utils import timezone
from requests_oauthlib import OAuth1Session
import requests.utils
import json
from .api_search import TwitterUtil
from .forms import SearchForm
from .sentiment_analysis import SentimentAnalysis
from .models import SentimentAnalysisModel
from .models import TweetSearch
import re
from operator import itemgetter
import datetime

def index(request):
	form = SearchForm()
	return render(request, 'index.html', {'form': form})

def procurar(request):
	if request.method == 'POST':
		form = SearchForm(request.POST or None)
		if form.is_valid():
			search = form.cleaned_data['search']
			field = form.cleaned_data['field']

			client = TwitterUtil()

			if not client.get_tweets("ifsc "+ search, 1000):
				return redirect(index_error)
			tweets = client.get_tweets("ifsc "+ search, 1000)

			list_tweet = []

			analysis = SentimentAnalysis()

			for tweet in range(0, len(tweets)):
				aux = tweets[tweet]['user']['location']

				if (re.search('brasil', aux, re.IGNORECASE) or re.search('Santa Catarina', aux, re.IGNORECASE)):
					list_tweet.append(tweets[tweet])
					analysis.score_sentiment(tweets[tweet]['text'])

			quantity = len(list_tweet)

			tweet_search = TweetSearch(time_was_made = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), count_tweets = quantity, tags = search)
			tweet_search.save()

			print("Atual search date: "+ datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

			client_analysis = SentimentAnalysisModel(positive = analysis.count_positive, default = analysis.count_default, negative = analysis.count_negative, tweet_search = tweet_search)
			client_analysis.save()

			if field == "oldest":
				list_tweet = sorted(list_tweet, key=lambda k: (len(k["id_str"]), int(k["id_str"][-2:])))
			if field == "morert":
				list_tweet = sorted(list_tweet, key = itemgetter('retweet_count'))
			if field == "minusrt":
				list_tweet = sorted(list_tweet, key = itemgetter('retweet_count'), reverse = True)

			return render(request, 'procurar.html', {'tweets': list_tweet, 'quantity': quantity, 'tags': search} )
	else:
		form = SearchForm()
		return render(request, 'index.html', {'form': form})

def graficos(request):
	sentiments_analysis = SentimentAnalysisModel.objects.last()

	#positive = sum([int(s.positive) for s in sentiments_analysis])
	#default = sum([int(s.default) for s in sentiments_analysis])
	#negative = sum([int(s.negative) for s in sentiments_analysis])

	positive = sentiments_analysis.positive
	default = sentiments_analysis.default
	negative = sentiments_analysis.negative

	context = {
		'positive': json.dumps(positive),
		'default': json.dumps(default),
		'negative': json.dumps(negative)
	}
	return render(request, 'graficos.html', context)

def history(request):
	table = TweetSearch.objects.all()
	return render(request, 'history.html', {'table': table})

def history_ajax(request):
	date = request.GET.get('date')
	print(date)
	tweet_search = TweetSearch.objects.get(time_was_made = date)

	ts = tweet_search.sentiments.all()

	for s in ts:
		p = s.positive
		d = s.default
		n = s.negative

	context = {
		'positive': json.dumps(p),
		'default': json.dumps(d),
		'negative': json.dumps(n)
	}

	request.session['context'] = context

	data = {'date': date}

	print(request.session['context'])

	return JsonResponse(context)

def index_error(request):
	form = SearchForm()
	return render(request, 'index.html', {'erro': 'Tag inválida! Tente novamente', 'form': form})
