#!/usr/bin/python3

from requests import get


def number_of_subscribers(subreddit):
    """Get the number of subscribers for a subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Check for any HTTP errors
        data = response.json()
        return data['data']['subscribers']
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return 0
