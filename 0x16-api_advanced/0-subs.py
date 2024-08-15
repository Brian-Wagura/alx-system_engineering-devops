#!/usr/bin/python3
"""
Function that queries the Reddit API
"""
import requests


def number_of_subscribers(subreddit):
    """
    Fetches the number of subscribers in a subreddit
    """
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        if 'subscribers' in data['data']:
            return (data['data']['subscribers'])
        else:
            return (0)
    else:
        return (0)
