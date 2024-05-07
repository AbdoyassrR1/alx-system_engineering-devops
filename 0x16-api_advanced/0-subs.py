#!/usr/bin/python3
"""
function that queries the Reddit API and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """Construct the URL for the subreddit's about page in JSON format"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    res = requests.get(url, headers={'User-Agent': 'app/1.0'})
    if res.status_code == 200:
        data = res.json()
        subscribers = data['data']['subscribers']
        return subscribers

    else:
        return 0
