# Generated by Django 2.1.7 on 2019-05-09 17:27

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TweetSearch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_was_made', models.DateTimeField(verbose_name='time made')),
                ('count_tweets', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AlterField(
            model_name='sentimentanalysismodel',
            name='default',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='sentimentanalysismodel',
            name='negative',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='sentimentanalysismodel',
            name='positive',
            field=models.CharField(max_length=1000),
        ),
        migrations.AddField(
            model_name='sentimentanalysismodel',
            name='tweet_search',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.TweetSearch'),
            preserve_default=False,
        ),
    ]
