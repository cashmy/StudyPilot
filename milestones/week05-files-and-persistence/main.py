import json
from pathlib import Path


DATA_FILE = Path(__file__).with_name("study_tasks.json")
BROKEN_FILE = Path(__file__).with_name("broken_study_tasks.json")
MISSING_FILE = Path(__file__).with_name("missing_study_tasks.json")


def build_sample_tasks():
    return [
        {
            "course_name": "Python Programming",
            "task_name": "Finish JSON practice",
            "priority": "high",
            "completed": False,
            "estimated_minutes": 40,
        },
        {
            "course_name": "History 101",
            "task_name": "Read chapter summary",
            "priority": "medium",
            "completed": True,
            "estimated_minutes": 30,
        },
        {
            "course_name": "Biology",
            "task_name": "Review cell vocabulary",
            "priority": "low",
            "completed": True,
            "estimated_minutes": 55,
        },
    ]


def save_tasks(file_path, task_list):
    with file_path.open("w", encoding="utf-8") as file:
        json.dump(task_list, file, indent=2)

    print("Saved", len(task_list), "tasks to", file_path.name)
    print()


def load_tasks(file_path):
    if not file_path.exists():
        print(file_path.name, "was not found. Returning an empty task list.")
        print()
        return []

    try:
        with file_path.open("r", encoding="utf-8") as file:
            loaded_data = json.load(file)
    except json.JSONDecodeError:
        print(
            file_path.name, "contains invalid JSON data. Returning an empty task list."
        )
        print()
        return []

    if not is_valid_task_list(loaded_data):
        print(
            file_path.name,
            "does not contain the expected task data. Returning an empty task list.",
        )
        print()
        return []

    print("Loaded", len(loaded_data), "tasks from", file_path.name)
    print()
    return loaded_data


def is_valid_task_list(loaded_data):
    if not isinstance(loaded_data, list):
        return False

    required_keys = [
        "course_name",
        "task_name",
        "priority",
        "completed",
        "estimated_minutes",
    ]

    for task in loaded_data:
        if not isinstance(task, dict):
            return False

        for key in required_keys:
            if key not in task:
                return False

    return True


def display_tasks(task_list, heading):
    print(heading)

    if not task_list:
        print("No tasks to display.")
        print()
        return

    for task in task_list:
        print("Course:", task["course_name"])
        print("Task:", task["task_name"])
        print("Priority:", task["priority"])
        print("Completed:", task["completed"])
        print("Estimated Minutes:", task["estimated_minutes"])
        print()


def write_broken_file(file_path):
    with file_path.open("w", encoding="utf-8") as file:
        file.write('{"course_name": "Broken Example", invalid json}')

    print("Created", file_path.name, "to demonstrate invalid file handling.")
    print()


def main():
    study_tasks = build_sample_tasks()

    print("StudyPilot - Week 5 Snapshot")
    print()

    display_tasks(study_tasks, "Tasks In Memory Before Saving")
    load_tasks(MISSING_FILE)

    save_tasks(DATA_FILE, study_tasks)
    loaded_tasks = load_tasks(DATA_FILE)
    display_tasks(loaded_tasks, "Tasks Loaded From JSON File")

    write_broken_file(BROKEN_FILE)
    load_tasks(BROKEN_FILE)


if __name__ == "__main__":
    main()
