from pathlib import Path

from services import (
    add_session_from_input,
    add_task_from_input,
    build_recommendations,
    build_summary,
    build_summary_endpoint_payload,
    build_tasks_endpoint_payload,
)
from storage import load_app_state, save_app_state
from views import (
    display_banner,
    display_json_preview,
    display_message,
    display_sessions,
    display_summary,
    display_tasks,
)


APP_FOLDER = Path(__file__).resolve().parent
DATA_FILE = APP_FOLDER / "studypilot_week06.json"


def seed_sample_data(app_state):
    if app_state["tasks"] or app_state["sessions"]:
        return False

    task_inputs = [
        {
            "course_name": "Python Programming",
            "topic": "JSON and architecture",
            "task_name": "Review architecture-preview notes",
            "priority": "high",
            "due_date": "2026-10-25",
            "estimated_minutes": 35,
            "completed": False,
        },
        {
            "course_name": "History 101",
            "topic": "Weekly reading",
            "task_name": "Summarize chapter highlights",
            "priority": "medium",
            "due_date": "2026-10-27",
            "estimated_minutes": 25,
            "completed": True,
        },
    ]

    session_inputs = [
        {
            "course_name": "Python Programming",
            "topic": "JSON and architecture",
            "minutes_studied": 30,
            "session_date": "2026-10-20",
            "notes": "Looked at how file roles split the same app idea.",
        },
        {
            "course_name": "History 101",
            "topic": "Weekly reading",
            "minutes_studied": 20,
            "session_date": "2026-10-21",
            "notes": "Finished the reading summary.",
        },
    ]

    for task_input in task_inputs:
        add_task_from_input(app_state, task_input)

    for session_input in session_inputs:
        add_session_from_input(app_state, session_input)

    return True


def main():
    app_state, message = load_app_state(DATA_FILE)

    display_banner()
    display_message(message)

    seeded_data = seed_sample_data(app_state)
    if seeded_data:
        display_message(
            "Week 6 seeded sample data so the architecture-preview files have something visible to work with."
        )
        saved, save_message = save_app_state(DATA_FILE, app_state)
        display_message(save_message)
        if not saved:
            display_message(
                "The in-memory data still exists even though saving failed."
            )

    summary = build_summary(app_state)
    recommendations = build_recommendations(summary)

    display_tasks(app_state["tasks"])
    display_sessions(app_state["sessions"])
    display_summary(summary, recommendations)
    display_json_preview(
        "Simulated JSON Response - GET /api/tasks",
        build_tasks_endpoint_payload(app_state),
    )
    display_json_preview(
        "Simulated JSON Response - GET /api/summary",
        build_summary_endpoint_payload(summary, recommendations),
    )


if __name__ == "__main__":
    main()
