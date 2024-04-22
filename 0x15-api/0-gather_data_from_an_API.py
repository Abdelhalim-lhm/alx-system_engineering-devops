#!/usr/bin/python3
""" script to get data from a REST API """
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]
    user_response = requests.get(url + "users/{}".format(user_id)).json()
    ids = {"userId": user_id}
    todos = requests.get(url + "todos", params=ids).json()
    task_done = []
    for todo in todos:
        if todo.get("completed") is True:
            task_done.append(todo.get("title"))
    print("Employee {} is done with tasks({}/{}):".format(
        user_response.get("name"), len(task_done), len(todos)))
    for done in task_done:
        print("\t {}".format(done))
