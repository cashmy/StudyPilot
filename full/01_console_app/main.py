from datetime import date
from pathlib import Path

from logic import (
    DUE_SOON_DAYS,
    ROLLING_SUMMARY_DAYS,
    build_progress_summary,
    build_recommendations,
    get_due_soon_tasks,
    get_incomplete_tasks,
    get_overdue_tasks,
    minutes_by_course,
    minutes_by_topic,
    parse_iso_date,
    sort_sessions,
    sort_tasks,
    total_minutes,
)
from storage import load_data, save_data


APP_FOLDER = Path(__file__).resolve().parent
DATA_FILE = APP_FOLDER / "studypilot_data.json"


def print_banner():
    print("\nStudyPilot")
    print("A small console study planner for tasks, sessions, and simple guidance.")


def pause():
    input("\nPress Enter to continue...")


def prompt_non_empty(label):
    while True:
        value = input(f"{label}: ").strip()
        if value:
            return value

        print("Please enter a value.")


def prompt_int(label, minimum=0):
    while True:
        value = input(f"{label}: ").strip()
        if not value.isdigit():
            print("Please enter a whole number.")
            continue

        number = int(value)
        if number < minimum:
            print(f"Please enter a number that is at least {minimum}.")
            continue

        return number


def prompt_date(label, allow_blank=False):
    while True:
        value = input(f"{label}: ").strip()

        if allow_blank and not value:
            return ""

        if parse_iso_date(value) is not None:
            return value

        print("Please enter a date in YYYY-MM-DD format.")


def prompt_priority():
    options = {
        "1": "high",
        "2": "medium",
        "3": "low",
        "high": "high",
        "medium": "medium",
        "low": "low",
    }

    while True:
        print("Priority options: 1 = high, 2 = medium, 3 = low")
        value = input("Priority: ").strip().lower()
        if value in options:
            return options[value]

        print("Please choose 1, 2, 3, high, medium, or low.")


def format_task_status(task):
    if task.get("completed", False):
        completed_date = task.get("completed_date", "")
        if completed_date:
            return f"Completed on {completed_date}"
        return "Completed"

    return "Open"


def display_tasks(tasks, title):
    print(f"\n{title}")
    print("-" * len(title))

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
    print(f"\n{title}")
    print("-" * len(title))

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
    print(f"\n{title}")
    if not totals:
        print("No totals available yet.")
        return

    for label, minutes in totals.items():
        print(f"- {label}: {minutes} min")


def find_task_by_id(tasks, task_id):
    for task in tasks:
        if task.get("id") == task_id:
            return task

    return None


def save_and_report(data):
    success, message = save_data(DATA_FILE, data)
    print(message)
    return success


def add_task_flow(data):
    print("\nAdd Study Task")
    print("--------------")

    task = {
        "id": data["next_task_id"],
        "course_name": prompt_non_empty("Course name"),
        "topic": prompt_non_empty("Topic"),
        "task_name": prompt_non_empty("Task name"),
        "priority": prompt_priority(),
        "due_date": prompt_date(
            "Due date (YYYY-MM-DD, press Enter to skip)", allow_blank=True
        ),
        "estimated_minutes": prompt_int("Estimated minutes", minimum=1),
        "completed": False,
        "completed_date": "",
    }

    data["tasks"].append(task)
    data["next_task_id"] += 1

    print(f"Added task #{task['id']}.")
    save_and_report(data)
    pause()


def view_tasks_flow(data):
    while True:
        print("\nView Tasks")
        print("----------")
        print("1. View all tasks")
        print("2. View incomplete tasks")
        print(f"3. View tasks due within {DUE_SOON_DAYS} days")
        print("4. View overdue tasks")
        print("0. Back")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            display_tasks(sort_tasks(data["tasks"]), "All Study Tasks")
            pause()
        elif choice == "2":
            display_tasks(get_incomplete_tasks(data["tasks"]), "Incomplete Study Tasks")
            pause()
        elif choice == "3":
            display_tasks(get_due_soon_tasks(data["tasks"]), "Tasks Due Soon")
            pause()
        elif choice == "4":
            display_tasks(get_overdue_tasks(data["tasks"]), "Overdue Tasks")
            pause()
        elif choice == "0":
            return
        else:
            print("Choose one of the menu numbers.")


def prompt_for_task_id(tasks, allow_blank=True):
    while True:
        prompt_text = "Enter the task ID"
        if allow_blank:
            prompt_text += " or press Enter to cancel"

        value = input(f"{prompt_text}: ").strip()

        if allow_blank and not value:
            return None

        if value.isdigit():
            return int(value)

        print("Please enter a valid task ID.")


def mark_task_completed_flow(data):
    incomplete_tasks = get_incomplete_tasks(data["tasks"])
    display_tasks(incomplete_tasks, "Incomplete Study Tasks")

    if not incomplete_tasks:
        pause()
        return

    task_id = prompt_for_task_id(incomplete_tasks)
    if task_id is None:
        print("No task was updated.")
        pause()
        return

    task = find_task_by_id(incomplete_tasks, task_id)
    if task is None:
        print("That task ID was not found in the incomplete task list.")
        pause()
        return

    task["completed"] = True
    task["completed_date"] = date.today().isoformat()

    print(f"Task #{task_id} marked as completed.")
    save_and_report(data)
    pause()


def remove_task_flow(data):
    all_tasks = sort_tasks(data["tasks"])
    display_tasks(all_tasks, "All Study Tasks")

    if not all_tasks:
        pause()
        return

    task_id = prompt_for_task_id(all_tasks)
    if task_id is None:
        print("No task was removed.")
        pause()
        return

    task = find_task_by_id(all_tasks, task_id)
    if task is None:
        print("That task ID was not found.")
        pause()
        return

    confirm = input(f"Remove task #{task_id}? (y/n): ").strip().lower()
    if confirm != "y":
        print("Task removal canceled.")
        pause()
        return

    data["tasks"].remove(task)
    print(f"Removed task #{task_id}.")
    save_and_report(data)
    pause()


def log_session_flow(data):
    print("\nLog Study Session")
    print("-----------------")

    session_date = prompt_date(
        "Session date (YYYY-MM-DD, press Enter for today)",
        allow_blank=True,
    )
    if not session_date:
        session_date = date.today().isoformat()

    session = {
        "id": data["next_session_id"],
        "course_name": prompt_non_empty("Course name"),
        "topic": prompt_non_empty("Topic"),
        "minutes_studied": prompt_int("Minutes studied", minimum=1),
        "session_date": session_date,
        "notes": input("Notes (optional): ").strip(),
    }

    data["sessions"].append(session)
    data["next_session_id"] += 1

    print(f"Logged session #{session['id']}.")
    save_and_report(data)
    pause()


def view_sessions_flow(data):
    sessions = sort_sessions(data["sessions"])
    display_sessions(sessions, "Study Sessions")

    print(f"\nTotal minutes studied: {total_minutes(sessions)}")
    display_totals("Minutes by Course", minutes_by_course(sessions))
    display_totals("Minutes by Topic", minutes_by_topic(sessions))
    pause()


def view_progress_summary_flow(data):
    summary = build_progress_summary(data["tasks"], data["sessions"])
    recommendations = build_recommendations(data["tasks"], data["sessions"])

    print(f"\nProgress Summary - Last {ROLLING_SUMMARY_DAYS} Days")
    print("--------------------------------")
    print(f"Open tasks: {summary['incomplete_task_count']}")
    print(
        f"Tasks completed in last {ROLLING_SUMMARY_DAYS} days: {summary['recently_completed_task_count']}"
    )
    print(f"Tasks due within {DUE_SOON_DAYS} days: {summary['due_soon_task_count']}")
    print(f"Overdue tasks: {summary['overdue_task_count']}")
    print(f"Estimated minutes remaining: {summary['estimated_remaining_minutes']}")
    print(
        f"Study sessions logged in last {ROLLING_SUMMARY_DAYS} days: {summary['recent_session_count']}"
    )
    print(
        f"Minutes studied in last {ROLLING_SUMMARY_DAYS} days: {summary['recent_minutes']}"
    )
    print(f"Minutes studied all time: {summary['all_time_minutes']}")

    difference = summary["estimated_remaining_minutes"] - summary["recent_minutes"]
    if difference > 0:
        print(
            f"Estimated remaining work is {difference} minutes higher than logged study time in the last {ROLLING_SUMMARY_DAYS} days."
        )
    elif difference < 0:
        print(
            f"You logged {-difference} more minutes in the last {ROLLING_SUMMARY_DAYS} days than your current estimated remaining work."
        )
    else:
        print("Your recent study time matches your current estimated remaining work.")

    display_totals(
        f"Minutes by Course - Last {ROLLING_SUMMARY_DAYS} Days",
        summary["recent_course_totals"],
    )
    display_totals(
        f"Minutes by Topic - Last {ROLLING_SUMMARY_DAYS} Days",
        summary["recent_topic_totals"],
    )

    print("\nRecommendations")
    print("---------------")
    for recommendation in recommendations:
        print(f"- {recommendation}")

    pause()


def save_data_flow(data):
    save_and_report(data)
    pause()


def reload_data_flow():
    confirm = (
        input(
            "Reload data from the JSON file and replace the current in-memory data? (y/n): "
        )
        .strip()
        .lower()
    )
    if confirm != "y":
        print("Reload canceled.")
        pause()
        return None

    data, message = load_data(DATA_FILE)
    print(message)
    pause()
    return data


def show_main_menu():
    print("\nMain Menu")
    print("---------")
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


def main():
    data, message = load_data(DATA_FILE)

    print_banner()
    print(message)

    while True:
        show_main_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_task_flow(data)
        elif choice == "2":
            view_tasks_flow(data)
        elif choice == "3":
            mark_task_completed_flow(data)
        elif choice == "4":
            remove_task_flow(data)
        elif choice == "5":
            log_session_flow(data)
        elif choice == "6":
            view_sessions_flow(data)
        elif choice == "7":
            view_progress_summary_flow(data)
        elif choice == "8":
            save_data_flow(data)
        elif choice == "9":
            reloaded_data = reload_data_flow()
            if reloaded_data is not None:
                data = reloaded_data
        elif choice == "0":
            save_and_report(data)
            print("Goodbye.")
            break
        else:
            print("Choose one of the menu numbers.")
            pause()


if __name__ == "__main__":
    main()
