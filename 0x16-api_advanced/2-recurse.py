#!/usr/bin/python3
"""returns a list containing the titles
of all hot articles for a given subreddit. """
import requests
from time import sleep


def recurse(subreddit, hot_list=[], after=[]):
    """returns a list containing the titles
    of all hot articles for a given subreddit. """
    sub = subreddit
    subreddit = "/r/{}/hot.json".format(sub)

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    if len(after) != 0:
        param = {"limit": 100, "after": after[-1]}
    else:
        param = {"limit": 100}

    sleep(1)
    query = "https://www.reddit.com{}".format(subreddit)
    res = requests.get(query, headers=headers, params=param)

    status = res.status_code

    if (status != 200):
        return None
    else:
        data = res.json()
        if data['data']['after'] in after:
            return hot_list
        after.append(data['data']['after'])
        posts = data["data"]['children']
        for post in posts:
            hot_list.append(post['data']['title'])

        return recurse(sub, hot_list, after)
