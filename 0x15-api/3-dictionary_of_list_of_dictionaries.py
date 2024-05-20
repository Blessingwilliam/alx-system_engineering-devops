import json
import requests

def fetch_data():
    # Fetch users
    users_response = requests.get("https://jsonplaceholder.typicode.com/users")
    users = users_response.json()

    # Fetch todos
    todos_response = requests.get("https://jsonplaceholder.typicode.com/todos")
    todos = todos_response.json()

    return users, todos

def main():
    users, todos = fetch_data()
    todo_dict = {}

    # Build the dictionary
    for user in users:
        user_id = user['id']
        username = user['username']
        user_todos = [todo for todo in todos if todo['userId'] == user_id]
        
        todo_dict[user_id] = [{
            "username": username,
            "task": todo['title'],
            "completed": todo['completed']
        } for todo in user_todos]

    # Write to JSON file
    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(todo_dict, json_file, indent=4)

if __name__ == "__main__":
    main()

