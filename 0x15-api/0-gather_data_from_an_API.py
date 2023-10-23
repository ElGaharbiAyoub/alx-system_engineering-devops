#!/usr/bin/python3
"""api"""
import requests
from sys import argv


def todo(userId):
    url_tasks = "https://jsonplaceholder.typicode.com/users/{}/todos"\
        .format(userId)
    url_name = "https://jsonplaceholder.typicode.com/users/{}".format(userId)
    tasks = requests.get(url_tasks).json()
    name = requests.get(url_name).json().get("name")
    tasksDone = ['\t {}\n'.format(dic.get('title')) for dic in tasks
                 if dic.get('completed')]

    if name and tasks:
        print("Employee {} is done with tasks({}/{}):".format(
            name, len(tasksDone), len(tasks)
        ))
        print(''.join(tasksDone), end='')


if __name__ == "__main__":
    if len(argv) == 2:
        todo(int(argv[1]))
