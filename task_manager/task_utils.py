from datetime import datetime

# Import validation functions
None

# Define tasks list
tasks = []
task = {"title": "Groceries",
 "description": "Shop at Market Basket for food", 
 "due_date": "2024-06-26",
 "completed": True}


# Implement add_task function
def add_task(title, description, due_date):
    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }

    tasks.append(task)
    print("Task added successfully!")


# Mark task complete
def mark_task_as_complete(index):
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        print("Task marked as complete!")
    else:
        print("Invalid task index.")


# View pending tasks
def view_pending_tasks():
    for task in tasks:
        if not task["completed"]:
            print(
                f"{task['title']} - Due: {task['due_date']}"
            )


# Calculate progress
def calculate_progress():
    if len(tasks) == 0:
        return 0
    completed = 0
    for task in tasks:
        if task["completed"]:
            completed += 1

    progress = (completed / len(tasks)) * 100
    return progress