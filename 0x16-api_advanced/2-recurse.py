#!/usr/bin/python3
"""Contains recursive function"""
import requests


def recurse(subreddit, hot_list=None, after=None):
    """
    Recursively fetches all hot articles from a given subreddit.
    """
    if hot_list is None:
        hot_list = []

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
            "User-Agent":
            "0x16-api_advanced:project:v1.0.0 (by /u/firdaus_cartoon_jr)"
            }
    params = {
            "limit": 100,
            "after": after
            }

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 404:
        return None

    try:
        data = response.json().get("data")
        if data is None or len(data.get("children", [])) == 0:
            return hot_list

        hot_list.extend([post.get("data").get("title")
                        for post in data.get("children")])
        after = data.get("after")

        if after is not None:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    except ValueError:
        return None
