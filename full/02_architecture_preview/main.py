from datetime import date
from pathlib import Path

from models import PRIORITY_OPTIONS
from services import (
    DUE_SOON_DAYS,
    add_session,
    add_task,
    build_progress_summary,
    build_recommendations,
    find_task_by_id,
    get_due_soon_tasks,
    get_incomplete_tasks,
    get_overdue_tasks,
    mark_task_completed,
    minutes_by_course,
    minutes_by_topic,
    parse_iso_date,
    remove_task,
    sort_sessions,
    sort_tasks,
    total_minutes,
)
from storage import load_data, save_data
from views import (
    display_banner,
    display_main_menu,
    display_message,
    display_progress_summary,
    display_sessions,
    display_task_menu,
    display_tasks,
    display_totals,
    display_heading,
    pause,
)


APP_FOLDER = Path(__file__).resolve().parent
DATA_FILE = APP_FOLDER / "studypilot_data.json"


def prompt_non_empty(label):
    while True:
        value = input(f"{label}: ").strip()
        if value:
            return value

        display_message("Please enter a value.")


def prompt_int(label, minimum=0):
    while True:
        value = input(f"{label}: ").strip()
        if not value.isdigit():
            display_message("Please enter a whole number.")
            continue

        number = int(value)
        if number < minimum:
            display_message(f"Please enter a number that is at least {minimum}.")
            continue

        return number


def prompt_date(label, allow_blank=False):
    while True:
        value = input(f"{label}: ").strip()

        if allow_blank and not value:
            return ""

        if parse_iso_date(value) is not None:
            return value

        display_message("Please enter a date in YYYY-MM-DD format.")


def prompt_priority():
    option_lookup = {}

    for index, priority in enumerate(PRIORITY_OPTIONS, start=1):
        option_lookup[str(index)] = priority
        option_lookup[priority] = priority

    while True:
        display_message("Priority options: 1 = high, 2 = medium, 3 = low")
        value = input("Priority: ").strip().lower()
        if value in option_lookup:
            return option_lookup[value]

        display_message("Please choose 1, 2, 3, high, medium, or low.")


def prompt_for_task_id(allow_blank=True):
    while True:
        prompt_text = "Enter the task ID"
        if allow_blank:
            prompt_text += " or press Enter to cancel"

        value = input(f"{prompt_text}: ").strip()

        if allow_blank and not value:
            return None

        if value.isdigit():
            return int(value)

        display_message("Please enter a valid task ID.")


def save_and_report(data):
    saved, message = save_data(DATA_FILE, data)
    display_message(message)
    return saved


def add_task_flow(data):
    display_heading("Add Study Task")

    task = add_task(
        data,
        course_name=prompt_non_empty("Course name"),
        topic=prompt_non_empty("Topic"),
        task_name=prompt_non_empty("Task name"),
        priority=prompt_priority(),
        due_date=prompt_date(
            "Due date (YYYY-MM-DD, press Enter to skip)",
            allow_blank=True,
        ),
        estimated_minutes=prompt_int("Estimated minutes", minimum=1),
    )

    display_message(f"Added task #{task['id']}.")
    save_and_report(data)
    pause()


def view_tasks_flow(data):
    while True:
        display_task_menu(DUE_SOON_DAYS)
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
            display_message("Choose one of the menu numbers.")


def mark_task_completed_flow(data):
    incomplete_tasks = get_incomplete_tasks(data["tasks"])
    display_tasks(incomplete_tasks, "Incomplete Study Tasks")

    if not incomplete_tasks:
        pause()
        return

    task_id = prompt_for_task_id()
    if task_id is None:
        display_message("No task was updated.")
        pause()
        return

    task = find_task_by_id(incomplete_tasks, task_id)
    if task is None:
        display_message("That task ID was not found in the incomplete task list.")
        pause()
        return

    mark_task_completed(task)
    display_message(f"Task #{task_id} marked as completed.")
    save_and_report(data)
    pause()


def remove_task_flow(data):
    all_tasks = sort_tasks(data["tasks"])
    display_tasks(all_tasks, "All Study Tasks")

    if not all_tasks:
        pause()
        return

    task_id = prompt_for_task_id()
    if task_id is None:
        display_message("No task was removed.")
        pause()
        return

    task = find_task_by_id(all_tasks, task_id)
    if task is None:
        display_message("That task ID was not found.")
        pause()
        return

    confirm = input(f"Remove task #{task_id}? (y/n): ").strip().lower()
    if confirm != "y":
        display_message("Task removal canceled.")
        pause()
        return

    remove_task(data, task)
    display_message(f"Removed task #{task_id}.")
    save_and_report(data)
    pause()


def log_session_flow(data):
    display_heading("Log Study Session")

    session_date = prompt_date(
        "Session date (YYYY-MM-DD, press Enter for today)",
        allow_blank=True,
    )
    if not session_date:
        session_date = date.today().isoformat()

    session = add_session(
        data,
        course_name=prompt_non_empty("Course name"),
        topic=prompt_non_empty("Topic"),
        minutes_studied=prompt_int("Minutes studied", minimum=1),
        session_date=session_date,
        notes=input("Notes (optional): ").strip(),
    )

    display_message(f"Logged session #{session['id']}.")
    save_and_report(data)
    pause()


def view_sessions_flow(data):
    sessions = sort_sessions(data["sessions"])
    display_sessions(sessions, "Study Sessions")
    display_message(f"\nTotal minutes studied: {total_minutes(sessions)}")
    display_totals("Minutes by Course", minutes_by_course(sessions))
    display_totals("Minutes by Topic", minutes_by_topic(sessions))
    pause()


def view_progress_summary_flow(data):
    summary = build_progress_summary(data["tasks"], data["sessions"])
    recommendations = build_recommendations(data["tasks"], data["sessions"])
    display_progress_summary(summary, recommendations, DUE_SOON_DAYS)
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
        display_message("Reload canceled.")
        pause()
        return None

    data, message = load_data(DATA_FILE)
    display_message(message)
    pause()
    return data


def main():
    data, message = load_data(DATA_FILE)

    display_banner()
    display_message(message)

    while True:
        display_main_menu()
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
            display_message("Goodbye.")
            break
        else:
            display_message("Choose one of the menu numbers.")
            pause()


if __name__ == "__main__":
    main()
