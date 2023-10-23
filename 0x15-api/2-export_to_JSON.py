#!/usr/bin/python3
"""api"""
import json
import requests
from sys import argv


def exportToCSV(userId):
    url_tasks = "https://jsonplaceholder.typicode.com/users/{}/todos"\
        .format(userId)
    url_name = "https://jsonplaceholder.typicode.com/users/{}".format(userId)
    tasks = requests.get(url_tasks).json()
    username = requests.get(url_name).json().get("username")
    data = []
    for obj in tasks:
        data.append(
            {"task": obj.get('title'), "completed": obj.get(
                'completed'), "username": username})
    csv_file = "{}.json".format(userId)
    with open(csv_file, mode='w', newline='') as file:
        json.dump({userId: data}, file)


if __name__ == "__main__":
    if len(argv) == 2:
        exportToCSV(int(argv[1]))
