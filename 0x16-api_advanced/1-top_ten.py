#!/usr/bin/python3
"""
Contains top_ten function
"""
import requests


def top_ten(subreddit):
    """
    prints the titles of the first 10 hot posts
    listed for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
            "User-Agent": "0x16-api_advanced:project:\
                    v1.0.0 (by /u/firdaus_cartoon_jr)"
            }
    params = {
            "limit": 10
            }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 404:
        print("None")
        return

    try:
        results = response.json().get("data")
        if results is not None:
            [print(c.get("data").get("title")) for c in results.get("children")]
        else:
            print(None)
    except ValueError:
        print(None)
