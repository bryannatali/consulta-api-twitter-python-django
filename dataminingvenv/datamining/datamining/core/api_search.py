import tweepy
import json
from requests_oauthlib import OAuth1Session
import urllib.parse

MAX_TWEETS = 100
BASE_URL = "https://api.twitter.com/1.1/search/tweets.json"

class TwitterUtil(object):
    consumer_key = "afIYOFpeqAYyiYan23HGNd4b8"
    consumer_secret = "ag86JE2RKzCY7seLrvwvIRPbnRbIWJaqa8N0MxaJLLtG3GmtsE"
    access_token = "3786972143-BGenQrHiLZJ18Ko8LxwIIwLkLJsRmCBCtsw5i2i"
    access_token_secret = "aKJQSkXYp0vYcx2MgxGdD5743cLo9vsxmXXFTqplzzuwq"

    def __init__(self):
        self.session = OAuth1Session(self.consumer_key,
                                     self.consumer_secret,
                                     self.access_token,
                                     self.access_token_secret)

    def get_tweets(self, keyword, n=15, max_id=None):
        list_keyword = keyword.split()
        for k in list_keyword:
            if k.isalpha()==False:
                return False
        if n > 0:
            url = BASE_URL + ("?q=%s&count=%d" % (urllib.parse.quote(keyword, safe=''), n))
            if max_id is not None:
                url = url + "&max_id=%d" % (max_id)
            response = self.session.get(url)
            if response.status_code == 200:
                tweets = json.loads(response.content)
                
                list_id = []
                for tweet in tweets['statuses']:
                    list_id.append(tweet['id'])

                if len(tweets['statuses']) <= 1:
                    return tweets['statuses']
                else:
                    oldest_id = min(list_id)
                    return tweets['statuses'] + \
                        self.get_tweets(keyword, n-MAX_TWEETS, oldest_id - 1)
        return []