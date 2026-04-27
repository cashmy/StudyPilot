import json


def display_banner():
    print("StudyPilot - Week 6 Snapshot")
    print("Architecture preview with simulated JSON-style responses")
    print()


def display_message(message):
    print(message)
    print()


def display_heading(title):
    print(title)
    print("-" * len(title))


def display_tasks(tasks):
    display_heading("Tasks")

    if not tasks:
        print("No tasks to display.")
        print()
        return

    for task in tasks:
        print(
            f"[{task['id']}] {task['course_name']} | {task['topic']} | {task['task_name']}"
        )
        print(
            f"    Priority: {task['priority']} | Due: {task['due_date'] or 'No due date'} | Completed: {task['completed']} | Estimated: {task['estimated_minutes']} min"
        )

    print()


def display_sessions(sessions):
    display_heading("Study Sessions")

    if not sessions:
        print("No sessions to display.")
        print()
        return

    for session in sessions:
        print(
            f"[{session['id']}] {session['session_date']} | {session['course_name']} | {session['topic']} | {session['minutes_studied']} min"
        )
        if session["notes"]:
            print(f"    Notes: {session['notes']}")

    print()


def display_summary(summary, recommendations):
    display_heading("Summary")
    print("Tasks:", summary["task_count"])
    print("Open tasks:", summary["open_task_count"])
    print("Completed tasks:", summary["completed_task_count"])
    print("Study sessions:", summary["session_count"])
    print("Minutes studied:", summary["minutes_studied"])
    print("Estimated open minutes:", summary["estimated_open_minutes"])
    print()

    display_heading("Recommendations")
    for recommendation in recommendations:
        print("-", recommendation)

    print()


def display_json_preview(title, payload):
    display_heading(title)
    print(json.dumps(payload, indent=2))
    print()
