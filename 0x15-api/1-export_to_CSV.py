#!/usr/bin/python3
""" script to get data from a REST API
    and export it to CSV file
"""
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]
    user_response = requests.get(url + "users/{}".format(user_id)).json()
    ids = {"userId": user_id}
    todos = requests.get(url + "todos", params=ids).json()
    file_name = "{}.csv".format(user_id)
    with open(file_name, "a") as file:
        for todo in todos:
            file.write('"{}","{}","{}","{}"\n'.format(
                user_id, user_response.get("name"), todo.get(
                    "completed"), todo.get("title")))
