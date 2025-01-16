# Project_02
import os
import json

# File to store task data
tasks_file = "tasks.json"

# Ensure the file exists
if not os.path.exists(tasks_file):
    with open(tasks_file, "w") as file:
        json.dump([], file)

def load_tasks():
    """Load tasks from the file."""
    with open(tasks_file, "r") as file:
        return json.load(file)

def save_tasks(tasks):
    """Save tasks to the file."""
    with open(tasks_file, "w") as file:
        json.dump(tasks, file)

def add_task():
    """Add a new task."""
    title = input("Enter the task title: ")
    description = input("Enter a brief description (optional): ")
    task = {"title": title, "description": description, "completed": False}
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!")

def view_tasks():
    """View all tasks."""
    tasks = load_tasks()
    if not tasks:
        print("\nNo tasks found.")
        return
    print("\nTo-Do List:")
    for i, task in enumerate(tasks, 1):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{i}. {task['title']} - {status}")
        if task["description"]:
            print(f"   Description: {task['description']}")

def mark_task_completed():
    """Mark a task as completed."""
    view_tasks()
    tasks = load_tasks()
    if not tasks:
        return
    try:
        task_num = int(input("\nEnter the task number to mark as completed: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["completed"] = True
            save_tasks(tasks)
            print("Task marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    """Delete a task."""
    view_tasks()
    tasks = load_tasks()
    if not tasks:
        return
    try:
        task_num = int(input("\nEnter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            deleted_task = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f"Task '{deleted_task['title']}' deleted successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    """Main menu for the To-Do List application."""
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_task_completed()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
