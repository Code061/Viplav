import os
import tweepy
from apscheduler.schedulers.blocking import BlockingScheduler  # type: ignore
from utils.sentiment_analysis import analyze_sentiment
from dotenv import load_dotenv
from datetime import datetime
import pytz  # type: ignore

load_dotenv()

# Twitter API credentials
API_KEY = os.getenv("API_KEY")
API_SECRET_KEY = os.getenv("API_SECRET_KEY")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")
BEARER_TOKEN = os.getenv("BEARER_TOKEN")

# Authenticate to Twitter using v2 API
client = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    consumer_key=API_KEY,
    consumer_secret=API_SECRET_KEY,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

# Verify authentication
try:
    user_response = client.get_me()
    if user_response.data:
        print(f"Authentication successful! Logged in as {user_response.data.username}")
    else:
        print("Authentication failed: Unable to retrieve user data.")
        exit()
except tweepy.TweepyException as e:
    print(f"Authentication failed: {e}")
    exit()

# Time zone setup
TIME_ZONE = pytz.timezone("Asia/Kolkata")  # Replace with your desired time zone

def tweet_greeting():
    current_time = datetime.now(TIME_ZONE).strftime("%Y-%m-%d %H:%M:%S")
    greeting_message = (
        f"Hello, world! I'm Viplav, your friendly agent of Aptoes. 🌟\n"
        f"Let's make today amazing! 😊\n"
        f"Current time: {current_time}"
    )
    print(f"Tweeting greeting at {current_time}")
    client.create_tweet(text=greeting_message)

def tweet_good_morning():
    current_time = datetime.now(TIME_ZONE).strftime("%Y-%m-%d %H:%M:%S")
    print(f"Tweeting Good Morning at {current_time}")
    client.create_tweet(text="Good Morning!")

def tweet_good_night():
    current_time = datetime.now(TIME_ZONE).strftime("%Y-%m-%d %H:%M:%S")
    print(f"Tweeting Good Night at {current_time}")
    client.create_tweet(text="Good Night!")

def respond_to_mentions():
    try:
        user_response = client.get_me()
        if user_response.data:
            mentions_response = client.get_users_mentions(user_response.data.id)
            if mentions_response.data:
                for mention in mentions_response.data:
                    sentiment_score, sentiment_label = analyze_sentiment(mention.text)
                    response = f"@{mention.author_id} Your tweet has a {sentiment_label} sentiment with a score of {sentiment_score}."
                    client.create_tweet(text=response, in_reply_to_tweet_id=mention.id)
    except tweepy.TweepyException as e:
        print(f"Error while responding to mentions: {e}")

# Scheduler setup
scheduler = BlockingScheduler()

# Schedule tasks
scheduler.add_job(tweet_good_morning, 'cron', hour=8, minute=0, timezone=TIME_ZONE)
scheduler.add_job(tweet_good_night, 'cron', hour=22, minute=0, timezone=TIME_ZONE)
scheduler.add_job(respond_to_mentions, 'interval', minutes=15)  # Check mentions every 15 minutes

if __name__ == "__main__":
    print("Starting the bot...")
    tweet_greeting()  # Post greeting when the bot starts
    scheduler.start()