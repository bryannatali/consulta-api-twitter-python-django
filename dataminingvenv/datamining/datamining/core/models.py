from django.db import models
from django import forms
import tweepy
import json
from requests_oauthlib import OAuth1Session
from operator import itemgetter

class SentimentAnalysis(object):
    sentilexpt = open(r"C:\Users\Admin\dev\SentiLex-lem-PT02.txt",'r')

    dic_palavra_polaridade = {}

    for i in sentilexpt.readlines():
        pos_ponto = i.find('.')
        palavra = (i[:pos_ponto])
        pol_pos = i.find('POL')
        polaridade = (i[pol_pos+4:pol_pos+6]).replace(';','')
        dic_palavra_polaridade[palavra] = polaridade

    def Score_sentimento(frase):
        frase = frase.lower()
        l_sentimento = []
        for p in frase.split():
            l_sentimento.append(int(dic_palavra_polaridade.get(p, 0)))
        score = sum(l_sentimento)
        if score > 0:
            return 'Positivo, Score:{}'.format(score)
        elif score == 0:
            return 'Neutro, Score:{}'.format(score)
        else:
            return 'Negativo, Score:{}'.format(score)