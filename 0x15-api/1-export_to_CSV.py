#!/usr/bin/python3
"""
export data in CSV format
Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
"""
import csv
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com"

    user = requests.get(f"{url}/users/{employee_id}").json()
    todos = requests.get(f"{url}/todos", params={'userId': employee_id}).json()
    file_name = employee_id + ".csv"

    with open(f"{employee_id}.csv", "w", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([employee_id, user.get('username'),
                            task.get('completed'), task.get('title')])
