import tweepy
from textblob import TextBlob as tb
import csv
import pandas as pd

# Step 1 - Authenticate
consumer_key= ''
consumer_secret= ''

access_token=''
access_token_secret=''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Step 3 - Retrieve Tweets
public_tweets = api.search('superbowl')

#Classify 

def classify(s):
	if s >= .15:
		return "Positive"
	elif s <= -.15:
		return "Negative"
	elif s <= .15and s >= -.15:
		return "Neutral"
	else:
		return "Not Defined"



output  = pd.DataFrame({"tweets":[], "polarity-value": [], "polarity": [], "subjectivity-value": [], "subjectivity": []})
col = ["tweets", "polarity-value", "polarity", "subjectivity-value", "subjectivity"]
for tweet in public_tweets:
	p = float(tb(tweet.text).sentiment.polarity)
	s = float(tb(tweet.text).sentiment.subjectivity)
	output.loc[len(output)] = [tweet.text.encode("utf-8"), p, classify(p), s, classify(s)]
output.columns = col
output.to_csv('output.csv', mode = 'w+', index = False)



	

