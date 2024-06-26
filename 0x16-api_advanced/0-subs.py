#!/usr/bin/python3
""" Function that queries the Reddit API """
import requests


def number_of_subscribers(subreddit):
    """get the number of subscribers to the subreddit"""
    headers = {'User-Agent': 'xica369'}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        return (response.json().get("data").get("subscribers"))
    return (0)
