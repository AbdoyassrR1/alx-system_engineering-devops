#!/usr/bin/python3
"""
returns information about employee's TO DO list.
"""
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com"

    user = requests.get(f"{url}/users/{employee_id}").json()
    todos = requests.get(f"{url}/todos", params={'userId': employee_id}).json()

    completed_tasks = []
    for task in todos:
        if task.get("completed"):
            completed_tasks.append(task)

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed_tasks), len(todos)))
    for todo in completed_tasks:
        print("\t " + todo.get("title"))
