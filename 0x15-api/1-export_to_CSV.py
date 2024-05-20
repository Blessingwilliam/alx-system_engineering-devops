#!/usr/bin/python3
"""
Returns to-do list information for a given employee ID and exports it to a CSV file.

This script takes an employee ID as a command-line argument and fetches
the corresponding user information and to-do list from the JSONPlaceholder API.
It then exports the data to a CSV file.
"""

import csv
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./1-export_to_CSV.py <employee_id>")
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
    username = user['username']

    # Get the to-do list for the employee using the provided employee ID
    todos_response = requests.get(url + "todos", params={"userId": employee_id})
    
    if todos_response.status_code != 200:
        print("Error fetching to-do list.")
        sys.exit(1)
    
    todos = todos_response.json()

    # Prepare CSV file name
    file_name = f"{employee_id}.csv"

    # Write data to CSV
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([employee_id, username, task['completed'], task['title']])

    print(f"Data for employee ID {employee_id} has been exported to {file_name}.")

