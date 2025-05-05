import tweepy
import pandas as pd


def run_twitter_etl():
    bearer_token = "YOUR_BEARER_TOKEN"  # Replace with your actual bearer token
    # Note: Ensure you have the correct permissions for your bearer token to access the Twitter API v2.

    # Set up Tweepy client (v2)
    client = tweepy.Client(bearer_token=bearer_token)

    # Search for recent public tweets about "football"
    response = client.search_recent_tweets(
        query="football -is:retweet",
        max_results=10,
        tweet_fields=["created_at", "public_metrics", "author_id"],
    )

    tweet_data = []
    if response.data:
        for tweet in response.data:
            metrics = tweet.public_metrics
            refined_tweet = {
                "tweet_id": tweet.id,
                "author_id": tweet.author_id,
                "text": tweet.text,
                "created_at": tweet.created_at,
                "retweet_count": metrics["retweet_count"],
                "like_count": metrics["like_count"],
            }
            tweet_data.append(refined_tweet)

        df = pd.DataFrame(tweet_data)
        df.to_csv("s3://aws_bucket_name/football_tweets.csv", index=False)
