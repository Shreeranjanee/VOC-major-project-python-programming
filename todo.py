import json

# Task class definition
class Task:
    def __init__(self, title, description, category):
        self.title = title
        self.description = description
        self.category = category
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "category": self.category,
            "completed": self.completed
        }

# Save tasks to a JSON file
def save_tasks(tasks):
    with open('tasks.json', 'w') as f:
        json.dump([task.to_dict() for task in tasks], f, indent=4)

# Load tasks from a JSON file
def load_tasks():
    try:
        with open('tasks.json', 'r') as f:
            return [Task(**data) for data in json.load(f)]
    except FileNotFoundError:
        return []

# Add a task
def add_task(tasks):
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    category = input("Enter task category (Work, Personal, Urgent): ")
    tasks.append(Task(title, description, category))
    print("Task added successfully!")

# View tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks):
            status = "Completed" if task.completed else "Pending"
            print(f"{i + 1}. {task.title} - {task.category} [{status}]")
            print(f"   Description: {task.description}")

# Mark a task as completed
def mark_task_completed(tasks):
    view_tasks(tasks)
    try:
        task_no = int(input("Enter task number to mark as completed: ")) - 1
        if 0 <= task_no < len(tasks):
            tasks[task_no].mark_completed()
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Delete a task
def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_no = int(input("Enter task number to delete: ")) - 1
        if 0 <= task_no < len(tasks):
            del tasks[task_no]
            print("Task deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main function to run the application
def main():
    tasks = load_tasks()

    while True:
        print("\nPersonal To-Do List")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Completed")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_task_completed(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Tasks saved. Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

# Entry point for the application
if __name__ == "__main__":
    main()
    