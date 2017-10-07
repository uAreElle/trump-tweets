import tweepy

# Populate Twitter API credentials below from https://apps.twitter.com/
consumer_key = "REPLACE-WITH-YOURS"
consumer_secret = "REPLACE-WITH-YOURS"
access_token_key = "REPLACE-WITH-YOURS"
access_token_secret = "REPLACE-WITH-YOURS"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)

api = tweepy.API(auth)

# Get list of latest 15 tweets (Status objects)
screen_name="realDonaldTrump"
max_tweets = 15
t = api.user_timeline(screen_name=screen_name, count=max_tweets, tweet_mode='extended')

ctr = 0
print "Printing 15 latest Trump tweets:"
for tweet in t:
	ctr += 1
	print "(" + str(ctr) + ")" + "[" + str(tweet.created_at) + "]"
	print tweet.full_text + "\n"
