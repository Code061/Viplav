from tweepy import OAuthHandler, API, Cursor
import os
from dotenv import load_dotenv

load_dotenv()

# Twitter API credentials from environment variables
API_KEY = os.getenv('API_KEY')
API_SECRET_KEY = os.getenv('API_SECRET_KEY')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')

# Authenticate to Twitter
def authenticate_twitter():
    auth = OAuthHandler(API_KEY, API_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    return API(auth)

# Post a tweet
def post_tweet(message):
    api = authenticate_twitter()
    api.update_status(message)

# Respond to a mention
def respond_to_mention(tweet_id, response):
    api = authenticate_twitter()
    api.update_status(status=response, in_reply_to_status_id=tweet_id, auto_populate_reply_metadata=True)