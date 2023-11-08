#!/usr/bin/python3
"""prints the titles of the first 10 hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts listed for a given subreddit
    """
    if subreddit is None:
        return 0
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    params = {
            "limit": 10
            }

    try:
        response = requests.get(url, params=params, headers=headers,
                                allow_redirects=False).json()
        data = response.get("data", {}).get("children", None)
        for topic in data:
            print(topic.get("data").get("title"))
    except requests.exceptions.RequestException as e:
        print("None")
