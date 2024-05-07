#!/usr/bin/python3
"""
function that queries the Reddit API and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """Construct the URL for the subreddit's about page in JSON format"""
    subscribers = requests.get(
                            f"https://www.reddit.com/r/{subreddit}/about.json",
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if subscribers.status_code == 200:
        return subscribers.json().get("data").get("subscribers")
    else:    
        return 0
