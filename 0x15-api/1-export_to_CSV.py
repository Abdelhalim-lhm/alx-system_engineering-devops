#!/usr/bin/python3
""" script to get data from a REST API
    and export it to CSV file
"""
import csv
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]
    user_response = requests.get(url + "users/{}".format(user_id)).json()
    ids = {"userId": user_id}
    todos = requests.get(url + "todos", params=ids).json()
    file_name = "{}.csv".format(user_id)
    with open(file_name, "w", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow([user_id, user_response.get("username"), todo.get(
                    "completed"), todo.get("title")])
