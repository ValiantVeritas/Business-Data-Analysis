import os
import sys
import tweepy
import requests
import numpy as np

from keras.models import Sequential
from keras.layers import Dense
from textblob import TextBlob as tb

consumer_key= ''
consumer_secret= ''

access_token=''
access_token_secret=''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

def stock_sentiment(company, num_tweets):
	tweets = user.search(quote, count = num_tweets)
	positive, null = 0, 0

	for tweet in tweets:
		sent = tb.(tweet.text).sentiment
		if sent.subjectivity == 0:
			null += 1
			next
		if sent.polarity > 0:
			positive += 1
	if positive > ((num_tweets- null)/2):
		return True


def get_historical(ticker):
	url = 'http://www.google.com/finance/historical?q=NASDAQ%3A'+ticker+'&output=csv'
	r = requests.get(url, stream=True)
	if r.status_code != 400:
		return r

