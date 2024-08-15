#!/usr/bin/python3
"""
Contains count_words function
"""
import requests
import re
from collections import defaultdict


def count_words(subreddit, word_list, counts=None, after=None):
    """
    Recursively fetches hot articles from a given subreddit
    and counts the occurrences
    of specified keywords in the titles.
    """
    if counts is None:
        counts = defaultdict(int)

    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
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
            return print_results(counts, word_list)

        for post in data.get("children"):
            title = post.get("data").get("title", "").lower()
            for word in word_list:
                pattern = r'\b' + re.escape(word.lower()) + r'\b'
                matches = re.findall(pattern, title)
                counts[word.lower()] += len(matches)

        after = data.get("after")
        if after is not None:
            return count_words(subreddit, word_list, counts, after)
        else:
            return print_results(counts, word_list)
    except ValueError:
        return None


def print_results(counts, word_list):
    """
    Prints the sorted results based on the counts.
    """
    filtered_counts = {word: counts[word]
                       for word in word_list if counts[word] > 0}
    sorted_counts = sorted(filtered_counts.items(),
                           key=lambda x: (-x[1], x[0]))

    for word, count in sorted_counts:
        print("{}:{}").format(word, count)
