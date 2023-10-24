import json                    //tasks.json should be created and initialized to []
import datetime

tasks = []

# Function to add a task to the list
def add_task():
    task = {}
    task['title'] = input("Enter the task title: ")
    task['description'] = input("Enter a description (optional): ")
    task['due_date'] = input("Enter the due date (YYYY-MM-DD): ")
    task['completed'] = False
    tasks.append(task)
    print("Task added successfully!")

# Function to list all tasks
def list_tasks():
    if tasks:
        print("\nTo-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. Title: {task['title']}")
            if task['description']:
                print(f"   Description: {task['description']}")
            if task['due_date']:
                print(f"   Due Date: {task['due_date']}")
            if task['completed']:
                print("   Status: Completed")
            else:
                print("   Status: Incomplete")
    else:
        print("No tasks in the list.")

# Function to mark a task as complete
def mark_complete():
    list_tasks()
    try:
        task_index = int(input("Enter the task number to mark as complete: ")) - 1
        if 0 <= task_index < len(tasks):
            tasks[task_index]['completed'] = True
            print(f"Marking '{tasks[task_index]['title']}' as complete.")
        else:
            print("Invalid task number. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

# Function to remove a task
def remove_task():
    list_tasks()
    try:
        task_index = int(input("Enter the task number to remove: ")) - 1
        if 0 <= task_index < len(tasks):
            removed_task = tasks.pop(task_index)
            print(f"Removing task: '{removed_task['title']}'")
        else:
            print("Invalid task number. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

# Function to update a task
def update_task():
    list_tasks()
    try:
        task_index = int(input("Enter the task number to update: ")) - 1
        if 0 <= task_index < len(tasks):
            task = tasks[task_index]
            print("Leave empty if you don't want to update a field.")
            new_title = input(f"New title for '{task['title']}': ")
            new_description = input(f"New description for '{task['title']}': ")
            new_due_date = input(f"New due date for '{task['title']}' (YYYY-MM-DD): ")
            
            if new_title:
                task['title'] = new_title
            if new_description:
                task['description'] = new_description
            if new_due_date:
                task['due_date'] = new_due_date
            
            print(f"Task '{task['title']}' updated.")
        else:
            print("Invalid task number. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

# Function to save tasks to a JSON file
def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)
    print("Tasks saved to 'tasks.json'")

# Function to load tasks from a JSON file
def load_tasks():
    global tasks
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
        print("Tasks loaded from 'tasks.json'")
    except FileNotFoundError:
        print("No task data found. Starting with an empty list.")

# Main program loop
load_tasks()

while True:
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Mark Task as Complete")
    print("4. Remove Task")
    print("5. Update Task")
    print("6. Save Tasks")
    print("7. Quit")
    
    choice = input("Enter your choice (1/2/3/4/5/6/7): ")
    
    if choice == '1':
        add_task()
    elif choice == '2':
        list_tasks()
    elif choice == '3':
        mark_complete()
    elif choice == '4':
        remove_task()
    elif choice == '5':
        update_task()
    elif choice == '6':
        save_tasks()
    elif choice == '7':
        break
    else:
        print("Invalid choice. Please enter a valid option.")

save_tasks()
