# Generated by Django 2.1.7 on 2019-05-09 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20190509_1439'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sentimentanalysismodel',
            name='tweet_search',
        ),
        migrations.DeleteModel(
            name='SentimentAnalysisModel',
        ),
        migrations.DeleteModel(
            name='TweetSearch',
        ),
    ]
