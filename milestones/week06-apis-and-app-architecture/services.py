from models import PRIORITY_OPTIONS, create_session, create_task


def next_id(records):
    highest_id = 0

    for record in records:
        record_id = record.get("id", 0)
        if isinstance(record_id, int) and record_id > highest_id:
            highest_id = record_id

    return highest_id + 1


def safe_minutes(value):
    if isinstance(value, int):
        return max(0, value)

    try:
        return max(0, int(value))
    except (TypeError, ValueError):
        return 0


def normalize_priority(value):
    priority = str(value).strip().lower()
    if priority in PRIORITY_OPTIONS:
        return priority

    return "medium"


def add_task_from_input(app_state, task_input):
    task = create_task(
        task_id=next_id(app_state["tasks"]),
        course_name=str(task_input.get("course_name", "")).strip(),
        topic=str(task_input.get("topic", "")).strip(),
        task_name=str(task_input.get("task_name", "")).strip(),
        priority=normalize_priority(task_input.get("priority", "medium")),
        due_date=str(task_input.get("due_date", "")).strip(),
        estimated_minutes=safe_minutes(task_input.get("estimated_minutes", 0)),
        completed=bool(task_input.get("completed", False)),
    )
    app_state["tasks"].append(task)
    return task


def add_session_from_input(app_state, session_input):
    session = create_session(
        session_id=next_id(app_state["sessions"]),
        course_name=str(session_input.get("course_name", "")).strip(),
        topic=str(session_input.get("topic", "")).strip(),
        minutes_studied=safe_minutes(session_input.get("minutes_studied", 0)),
        session_date=str(session_input.get("session_date", "")).strip(),
        notes=str(session_input.get("notes", "")).strip(),
    )
    app_state["sessions"].append(session)
    return session


def get_open_tasks(tasks):
    return [task for task in tasks if not task.get("completed", False)]


def get_completed_tasks(tasks):
    return [task for task in tasks if task.get("completed", False)]


def total_minutes(sessions):
    minutes = 0

    for session in sessions:
        minutes = minutes + safe_minutes(session.get("minutes_studied", 0))

    return minutes


def build_summary(app_state):
    open_tasks = get_open_tasks(app_state["tasks"])
    completed_tasks = get_completed_tasks(app_state["tasks"])
    minutes_studied = total_minutes(app_state["sessions"])

    return {
        "task_count": len(app_state["tasks"]),
        "open_task_count": len(open_tasks),
        "completed_task_count": len(completed_tasks),
        "session_count": len(app_state["sessions"]),
        "minutes_studied": minutes_studied,
        "estimated_open_minutes": sum(
            safe_minutes(task.get("estimated_minutes", 0)) for task in open_tasks
        ),
    }


def build_recommendations(summary):
    recommendations = []

    if summary["open_task_count"]:
        recommendations.append(
            "Open tasks still remain, so StudyPilot would next focus on task filtering or task-complete actions."
        )

    if summary["minutes_studied"] == 0:
        recommendations.append(
            "No study time has been logged yet, so a next step could be adding a session through structured input."
        )

    if summary["estimated_open_minutes"] > summary["minutes_studied"]:
        recommendations.append(
            "Estimated open work is still higher than logged study time."
        )

    if not recommendations:
        recommendations.append(
            "This milestone is mainly about recognizing file roles and JSON-style responses, not expanding feature count."
        )

    return recommendations


def build_tasks_endpoint_payload(app_state):
    return {
        "endpoint": "GET /api/tasks",
        "count": len(app_state["tasks"]),
        "tasks": app_state["tasks"],
    }


def build_summary_endpoint_payload(summary, recommendations):
    return {
        "endpoint": "GET /api/summary",
        "summary": summary,
        "recommendations": recommendations,
    }
