#!/usr/bin/python3
"""
A Script that, uses this REST API,
for a given employee ID, returns
information about his/her TODO list progress
"""

import json
import requests
import sys


employee_url = "https://jsonplaceholder.typicode.com/users/" + sys.argv[1]
todos = employee_url + "/todos"


employee = requests.get(employee_url)
emp_json = employee.json()


todo = requests.get(todos)
todo_json = todo.json()

EMPLOYEE_NAME = emp_json["name"]

TOTAL_NUMBER_OF_TASKS = len(todo_json)

completed = []

for item in todo_json:
    if item["completed"]:
        completed.append(item)

NUMBER_OF_DONE_TASKS = len(completed)

print(f"Employee {EMPLOYEE_NAME} is done with tasks"
      "({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")
for item in completed:
    print("\t" + item["title"])
