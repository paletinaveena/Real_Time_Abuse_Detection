import tweepy
from datetime import datetime
from app.config import BEARER_TOKEN
from app.database import get_db_connection
from app.abuse_detection import run_rules, AbuseClassifier
from app.moderation import flag_post
import time

# Tweepy client using bearer token (Free Access)
client = tweepy.Client(bearer_token=BEARER_TOKEN)

# Define keywords to look for in tweets
QUERY = "abuse OR hate OR violence OR horrible -is:retweet lang:en"

# Initialize classifier
classifier = AbuseClassifier()

def search_and_process():
    print("🔍 Searching recent tweets...")

    try:
        response = client.search_recent_tweets(
            query=QUERY,
            max_results=10,
            tweet_fields=["created_at", "text"]
        )
    except tweepy.TooManyRequests:
        print("⚠️ Rate limit hit. Waiting 15 minutes before retrying...")
        time.sleep(15 * 60)  # Wait 15 minutes
        return

