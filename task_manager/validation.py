from datetime import datetime



def validate_task_title(title):
    """
    Validates that the task title is a non-empty string.
    """
    if not isinstance(title, str):
        raise ValueError("Task title must be a string.")

    if title.strip() == "":
        raise ValueError("Task title cannot be empty.")

    return True


def validate_task_description(description):
    """
    Validates that the task description is a non-empty string.
    """
    if not isinstance(description, str):
        raise ValueError("Task description must be a string.")

    if description.strip() == "":
        raise ValueError("Task description cannot be empty.")

    return True


def validate_due_date(due_date):
    """
    Validates that the due date follows YYYY-MM-DD format.
    """
    if not isinstance(due_date, str):
        raise ValueError("Due date must be a string.")

    try:
        datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        raise ValueError(
            "Invalid due date format. Use YYYY-MM-DD."
        )

    return True