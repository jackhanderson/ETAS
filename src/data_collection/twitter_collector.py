import tweepy
import os
from dotenv import load_dotenv
from datetime import datetime
import logging

class TwitterCollector:
    def __init__(self):
        load_dotenv()
        
        # Configure logging
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        
        # Initialize Twitter API
        self.client = tweepy.Client(
            bearer_token=os.getenv('TWITTER_BEARER_TOKEN'),
            consumer_key=os.getenv('TWITTER_API_KEY'),
            consumer_secret=os.getenv('TWITTER_API_SECRET'),
            access_token=os.getenv('TWITTER_ACCESS_TOKEN'),
            access_token_secret=os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
        )

    def search_tweets(self, query, max_results=20):
        """
        Search for tweets matching the query
        """
        try:
            tweets = self.client.search_recent_tweets(
                query=query,
                max_results=max_results,
                tweet_fields=['created_at', 'lang', 'geo']
            )
            
            if not tweets.data:
                self.logger.info(f"No tweets found for query: {query}")
                return []
            
            # Format tweets for storage
            formatted_tweets = [
                {
                    'id': tweet.id,
                    'text': tweet.text,
                    'created_at': tweet.created_at,
                    'lang': tweet.lang,
                    'geo': tweet.geo,
                    'query': query
                }
                for tweet in tweets.data
            ]
            
            self.logger.info(f"Found {len(formatted_tweets)} tweets for query: {query}")
            return formatted_tweets
            
        except Exception as e:
            self.logger.error(f"Error searching tweets: {str(e)}")
            return []

    def get_naval_activity_tweets(self):
        """
        Search for tweets related to naval activities
        """
        search_queries = [
            "naval exercise",
            "maritime exercise",
            "fleet movement",
            "naval deployment",
            "Pacific fleet",
            "South China Sea navy",
            "naval operations"
        ]
        
        all_tweets = []
        for query in search_queries:
            tweets = self.search_tweets(query)
            all_tweets.extend(tweets)
            
        return all_tweets