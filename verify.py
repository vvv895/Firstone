import os,tweepy

CONSUMER_KEY = "dkedjekdjekldjekldje"
CONSUMER_SECRET = "dkejkdjekdjkejdkjekdjekjdkjed"


# Authenticate to Twitter
auth = tweepy.OAuthHandler("CONSUMER_KEY", "CONSUMER_SECRET")
auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")

ACCESS_TOKEN="123;j23k"
ACCESS_TOKEN_SECRET="asdlkfje"

# Create API object
api = tweepy.API(auth)

# Create a tweet
api.update_status("Hello Tweepy")
