#!/usr/bin/python3
"""Simple example of exporting user data to json"""

import json
import requests
from sys import argv as av


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/users/"

    user_data = requests.get(base_url + "{}".format(av[1])).json()
    todo_data = requests.get(base_url + "{}/todos".format(av[1])).json()

    user_id = av[1]
    user_tasks = []

    # collect all json data into a list that we write to the file
    for todo in todo_data:
        task = {
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": user_data.get("username")
                }
        user_tasks.append(task)

    format = {user_id: user_tasks}

    with open("{}.json".format(user_id), "w") as file:
        json.dump(format, file)
