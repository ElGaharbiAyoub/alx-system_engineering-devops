#!/usr/bin/python3
"""api"""
import csv
import requests
from sys import argv


def exportToCSV(userId):
    url_tasks = "https://jsonplaceholder.typicode.com/users/{}/todos"\
        .format(userId)
    url_name = "https://jsonplaceholder.typicode.com/users/{}".format(userId)
    tasks = requests.get(url_tasks).json()
    name = requests.get(url_name).json().get("username")

    if name and tasks:
        csv_file = "{}.csv".format(userId)
        with open(csv_file, mode='w', newline='') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_ALL)
            for row in tasks:
                writer.writerow(
                    [row.get('userId'), name,  row.get(
                        'completed'), row.get('title')])


if __name__ == "__main__":
    if len(argv) == 2:
        exportToCSV(int(argv[1]))
