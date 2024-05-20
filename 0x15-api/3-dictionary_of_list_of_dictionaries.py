import json
import requests

# URLs to fetch the data
users_url = 'https://jsonplaceholder.typicode.com/users'
todos_url = 'https://jsonplaceholder.typicode.com/todos'

# Fetch users data
users_response = requests.get(users_url)
users_data = users_response.json()

# Fetch todos data
todos_response = requests.get(todos_url)
todos_data = todos_response.json()

# Prepare the dictionary to store the tasks for each user
tasks_by_user = {}

# Populate the dictionary
for user in users_data:
    user_id = user['id']
    username = user['username']
    tasks_by_user[user_id] = []

    # Find the tasks for the current user
    for todo in todos_data:
        if todo['userId'] == user_id:
            task_info = {
                "username": username,
                "task": todo['title'],
                "completed": todo['completed']
            }
            tasks_by_user[user_id].append(task_info)

# Export the data to a JSON file
with open('todo_all_employees.json', 'w') as json_file:
    json.dump(tasks_by_user, json_file, indent=4)

print("Data exported to todo_all_employees.json")

