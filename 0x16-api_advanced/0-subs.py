#!/usr/bin/python3
"""Get the number of subscribers for a subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Get the number of subscribers for a subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        return data.get('data', {}).get('subscribers', 0)
    except requests.exceptions.RequestException as e:
        return 0
