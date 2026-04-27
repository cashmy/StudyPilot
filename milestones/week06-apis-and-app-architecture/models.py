PRIORITY_OPTIONS = ("high", "medium", "low")


def create_app_state():
    return {
        "tasks": [],
        "sessions": [],
    }


def create_task(
    task_id,
    course_name,
    topic,
    task_name,
    priority,
    due_date,
    estimated_minutes,
    completed=False,
):
    return {
        "id": task_id,
        "course_name": course_name,
        "topic": topic,
        "task_name": task_name,
        "priority": priority,
        "due_date": due_date,
        "estimated_minutes": estimated_minutes,
        "completed": completed,
    }


def create_session(
    session_id,
    course_name,
    topic,
    minutes_studied,
    session_date,
    notes,
):
    return {
        "id": session_id,
        "course_name": course_name,
        "topic": topic,
        "minutes_studied": minutes_studied,
        "session_date": session_date,
        "notes": notes,
    }
