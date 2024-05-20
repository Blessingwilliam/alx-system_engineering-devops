#!/usr/bin/python3
"""
Returns to-do list information for a given employee ID.

This script takes an employee ID as a command-line argument and fetches
the corresponding user information and to-do list from the JSONPlaceholder API.
It then prints the tasks completed by the employee.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)
    
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    # Base URL for the JSONPlaceholder API
    url = "https://jsonplaceholder.typicode.com/"

    # Get the employee information using the provided employee ID
    user_response = requests.get(url + f"users/{employee_id}")
    
    if user_response.status_code != 200:
        print("Employee not found.")
        sys.exit(1)
    
    user = user_response.json()

    # Get the to-do list for the employee using the provided employee ID
    todos_response = requests.get(url + "todos", params={"userId": employee_id})
    
    if todos_response.status_code != 200:
        print("Error fetching to-do list.")
        sys.exit(1)
    
    todos = todos_response.json()

    # Filter completed tasks and count them
    completed_tasks = [task["title"] for task in todos if task["completed"]]
    total_tasks = len(todos)
    completed_count = len(completed_tasks)

    # Print the employee's name and the number of completed tasks
    print(f"Employee {user['name']} is done with tasks({completed_count}/{total_tasks}):")
    
    # Print the completed tasks one by one with indentation
    for task in completed_tasks:
        print(f"\t {task}")

