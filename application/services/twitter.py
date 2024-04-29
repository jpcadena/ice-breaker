"""
A module for twitter in the application.services package.
"""

import logging

import tweepy
from pydantic import PositiveInt

from application.config import settings

logger: logging.Logger = logging.getLogger("twitter")

twitter_client = tweepy.Client(
    bearer_token=settings.TWITTER_BEARER_TOKEN,
    consumer_key=settings.TWITTER_API_KEY,
    consumer_secret=settings.TWITTER_API_SECRET,
    access_token=settings.TWITTER_ACCESS_TOKEN,
    access_token_secret=settings.TWITTER_ACCESS_SECRET,
)


def scrape_user_tweets(
    username: str, num_tweets: PositiveInt = 5
) -> list[dict[str, str]]:
    """
    Scrapes a Twitter user's original tweets (i.e., not retweets or replies)
    :param username: Twitter username
    :type username: str
    :param num_tweets: The number of tweets
    :type num_tweets: PositiveInt
    :return: Users as a list of dictionaries
    :rtype: list[dict[str, str]]
    """
    user_id = twitter_client.get_user(username=username).data.id
    tweets = twitter_client.get_users_tweets(
        id=user_id, max_results=num_tweets, exclude=["retweets", "replies"]
    )
    tweet_list: list[dict[str, str]] = []
    for tweet in tweets.data:
        tweet_dict = {
            "text": tweet["text"],
            "url": f"{settings.TWITTER_BASE_ENDPOINT}{username}/status/"
            f"{tweet.id}",
        }
        tweet_list.append(tweet_dict)
    return tweet_list
