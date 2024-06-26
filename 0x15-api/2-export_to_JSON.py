#!/usr/bin/python3
""" script to get data from a REST API
    and export it to json file
"""
import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]
    user_response = requests.get(url + "users/{}".format(user_id)).json()
    ids = {"userId": user_id}
    todos = requests.get(url + "todos", params=ids).json()
    file_name = "{}.json".format(user_id)
    user_dict = {user_id: []}
    for todo in todos:
        todo_dict = {"task": todo.get(
            "title"), "completed": todo.get(
                "completed"), "username": user_response.get(
                    "username")}
        user_dict[user_id].append(todo_dict)
    with open(file_name, "w") as file:
        json.dump(user_dict, file)
