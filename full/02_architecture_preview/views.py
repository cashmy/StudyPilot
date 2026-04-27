def display_message(message):
    print(message)


def display_heading(title):
    print(f"\n{title}")
    print("-" * len(title))


def display_banner():
    print("\nStudyPilot")
    print(
        "Architecture preview: the same study planner with clearer file responsibilities."
    )


def pause():
    input("\nPress Enter to continue...")


def display_main_menu():
    display_heading("Main Menu")
    print("1. Add study task")
    print("2. View study tasks")
    print("3. Mark task as completed")
    print("4. Remove study task")
    print("5. Log study session")
    print("6. View study sessions")
    print("7. View progress summary and recommendations")
    print("8. Save data now")
    print("9. Reload data from file")
    print("0. Exit")


def display_task_menu(due_soon_days):
    display_heading("View Tasks")
    print("1. View all tasks")
    print("2. View incomplete tasks")
    print(f"3. View tasks due within {due_soon_days} days")
    print("4. View overdue tasks")
    print("0. Back")


def format_task_status(task):
    if task.get("completed", False):
        completed_date = task.get("completed_date", "")
        if completed_date:
            return f"Completed on {completed_date}"
        return "Completed"

    return "Open"


def display_tasks(tasks, title):
    display_heading(title)

    if not tasks:
        print("No tasks to show.")
        return

    for task in tasks:
        due_text = task.get("due_date") or "No due date"
        print(
            f"[{task.get('id')}] {task.get('course_name')} | {task.get('topic')} | {task.get('task_name')}"
        )
        print(
            "    "
            f"Priority: {str(task.get('priority', 'medium')).title()} | "
            f"Due: {due_text} | "
            f"Estimated: {task.get('estimated_minutes', 0)} min | "
            f"Status: {format_task_status(task)}"
        )


def display_sessions(sessions, title):
    display_heading(title)

    if not sessions:
        print("No study sessions logged yet.")
        return

    for session in sessions:
        print(
            f"[{session.get('id')}] {session.get('session_date')} | "
            f"{session.get('course_name')} | {session.get('topic')} | "
            f"{session.get('minutes_studied', 0)} min"
        )

        notes = session.get("notes", "").strip()
        if notes:
            print(f"    Notes: {notes}")


def display_totals(title, totals):
    display_heading(title)

    if not totals:
        print("No totals available yet.")
        return

    for label, minutes in totals.items():
        print(f"- {label}: {minutes} min")


def display_progress_summary(summary, recommendations, due_soon_days):
    summary_days = summary["summary_days"]

    display_heading(f"Progress Summary - Last {summary_days} Days")
    print(f"Open tasks: {summary['incomplete_task_count']}")
    print(
        f"Tasks completed in last {summary_days} days: {summary['recently_completed_task_count']}"
    )
    print(f"Tasks due within {due_soon_days} days: {summary['due_soon_task_count']}")
    print(f"Overdue tasks: {summary['overdue_task_count']}")
    print(f"Estimated minutes remaining: {summary['estimated_remaining_minutes']}")
    print(
        f"Study sessions logged in last {summary_days} days: {summary['recent_session_count']}"
    )
    print(f"Minutes studied in last {summary_days} days: {summary['recent_minutes']}")
    print(f"Minutes studied all time: {summary['all_time_minutes']}")

    difference = summary["estimated_remaining_minutes"] - summary["recent_minutes"]
    if difference > 0:
        print(
            f"Estimated remaining work is {difference} minutes higher than logged study time in the last {summary_days} days."
        )
    elif difference < 0:
        print(
            f"You logged {-difference} more minutes in the last {summary_days} days than your current estimated remaining work."
        )
    else:
        print("Your recent study time matches your current estimated remaining work.")

    display_totals(
        f"Minutes by Course - Last {summary_days} Days",
        summary["recent_course_totals"],
    )
    display_totals(
        f"Minutes by Topic - Last {summary_days} Days",
        summary["recent_topic_totals"],
    )

    display_heading("Recommendations")
    for recommendation in recommendations:
        print(f"- {recommendation}")
