from django.db import models
from django import forms
import tweepy
import json
from requests_oauthlib import OAuth1Session
from operator import itemgetter
from django.contrib.contenttypes.fields import GenericRelation

class TweetSearch(models.Model):
	time_was_made = models.DateTimeField('time made')
	count_tweets = models.IntegerField()

	def set_search(self, time, count):
		self.time_was_made = time
		self.count_tweets = count

class SentimentAnalysisModel(models.Model):
    positive = models.IntegerField()
    default = models.IntegerField()
    negative = models.IntegerField()
    tweet_search = models.ForeignKey(TweetSearch, related_name='sentiments', on_delete=models.CASCADE)



#s = SentimentAnalysisModel.objects.last()
#t = TweetSearch.objects.last()
#ts = t.sentiments.all()