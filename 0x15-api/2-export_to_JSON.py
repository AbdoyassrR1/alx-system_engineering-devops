#!/usr/bin/python3
"""
export data in JSON format
"""
import json
import requests
import sys


if __name__ == "__main__":

    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    tasks_dict = {user_id: []}
    for todo in todos:
        tasks_dict[user_id].append({
            "task": todo.get("title"),
            "completed": todo.get("completedcompleted"),
            "username": username
        })

    with open("{}.json".format(user_id), "w") as file:
        json.dump(tasks_dict, file)
