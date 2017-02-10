import os
import sys
import tweepy
import requests
import numpy as np
import pandas as pd
import io

from keras.models import Sequential
from keras.layers import Dense
from textblob import TextBlob as tb

consumer_key= ''
consumer_secret= ''

access_token=''
access_token_secret=''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
user = tweepy.API(auth)
#retrieve 100 tweets regarding the company, judge if sentiment is positive or negative
#and return whether or not the model's prediction matches sentiment on twitter
	tweets = user.search(company, count = num_tweets)
	positive, null = 0, 0

	for tweet in tweets:
		sent = tb(tweet.text).sentiment
		if sent.subjectivity == 0:
			null += 1
			next
		if sent.polarity > 0:
			positive += 1
	ispositive = positive > ((num_tweets- null)/2)
	test = (bullish, ispositive)
	result = {
		(True, True): "a rise in stock price is supported by positive sentiment on twitter",
		(True, False): "however, there is negative sentiment regarding this company on twitter\nwhich may indicate a fall stock price",
		(False, False): "a fall in stock price is supported by negative sentiment on twitter",
		(False, True): "however, there is positive sentiment regarding this company on twitter\nwhich may indicate a rise in stock price"
	}
	return result.get(test)
	

#take a stock ticker, download its historical data in csv format and return it as a pandas data frame
def get_historical(ticker):
	url = 'http://www.google.com/finance/historical?q=NASDAQ%3A'+ticker+'&output=csv'
	r = requests.get(url, stream=True)
	if r.status_code != 400:
		data = pd.read_csv(io.StringIO(r.content.decode('utf-8')))
		return data
	elif r.status_code == 400:
		print 'Google returned a 404, please re-run the script and enter a valid stock quote from NASDAQ'
		sys.exit
#read a data frame containing historical price data, feed it into a model and return a prediction for opening stock price tomorrow
# and whether or not the stock price will rise
def stock_prediction(df):
	dataset = df["Open"].values
	def create_dataset(dataset):
		dataX = [dataset[n+1] for n in range(len(dataset)-2)]
		return np.array(dataX), dataset[2:]
        
	trainX, trainY = create_dataset(dataset)

    # Create and fit Multilinear Perceptron model
	model = Sequential()
	model.add(Dense(8, input_dim=1, activation='relu'))
	model.add(Dense(1))
	model.compile(loss='mean_squared_error', optimizer='adam')
	model.fit(trainX, trainY, nb_epoch=200, batch_size=2, verbose=2)

	# Our prediction for tomorrow
	prediction = model.predict(np.array([dataset[0]]))
	bullish = True if (dataset[0] - prediction[0][0]) < 0 else False
	result = 'The price will move from %s to %s' % (dataset[0], prediction[0][0])

	return result, bullish
stock_quote = raw_input('Enter a stock quote from NASDAQ (e.j: AAPL, FB, GOOGL): ').upper()
company_name = raw_input('Enter the company name: ')
final_result = stock_prediction(get_historical(stock_quote))
#print the predicted price
print(final_result[0])
#print twitters sentiment and whether it aligns with the prediction
print(stock_sentiment(company_name, 100, final_result[1]))

