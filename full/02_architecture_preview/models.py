PRIORITY_OPTIONS = ("high", "medium", "low")


def create_app_data():
    return {
        "next_task_id": 1,
        "next_session_id": 1,
        "tasks": [],
        "sessions": [],
    }


def next_record_id(records):
    highest_id = 0

    for record in records:
        record_id = record.get("id", 0)
        if isinstance(record_id, int) and record_id > highest_id:
            highest_id = record_id

    return highest_id + 1


def create_task(
    task_id,
    course_name,
    topic,
    task_name,
    priority,
    due_date,
    estimated_minutes,
    completed=False,
    completed_date="",
):
    return {
        "id": task_id,
        "course_name": course_name.strip(),
        "topic": topic.strip(),
        "task_name": task_name.strip(),
        "priority": priority,
        "due_date": due_date,
        "estimated_minutes": estimated_minutes,
        "completed": completed,
        "completed_date": completed_date,
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
        "course_name": course_name.strip(),
        "topic": topic.strip(),
        "minutes_studied": minutes_studied,
        "session_date": session_date,
        "notes": notes.strip(),
    }
