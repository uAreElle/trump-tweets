# Requirement:	pip install python-twitter

import twitter

# Populate Twitter API details below from https://apps.twitter.com/
consumer_key = "REPLACE-WITH-YOURS"
consumer_secret = "REPLACE-WITH-YOURS"
access_token_key = "REPLACE-WITH-YOURS"
access_token_secret = "REPLACE-WITH-YOURS"

api = twitter.Api(
	consumer_key = consumer_key,
	consumer_secret = consumer_secret,
	access_token_key = access_token_key,
	access_token_secret = access_token_secret
)

# Get list of latest 20 tweets (Status objects)
t = api.GetUserTimeline(screen_name='realDonaldTrump', count=20) 

ctr = 0
print "Printing 20 latest Trump tweets:"
for tweet in t:
	ctr += 1
	print "(" + str(ctr) + ")" + "[" + tweet.created_at + "]"
	print tweet.text + "\n"