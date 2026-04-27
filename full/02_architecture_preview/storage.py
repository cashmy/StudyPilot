import json
from pathlib import Path

from models import create_app_data, next_record_id


def normalize_data(data):
    cleaned_data = create_app_data()

    if not isinstance(data, dict):
        return cleaned_data

    tasks = data.get("tasks", [])
    if isinstance(tasks, list):
        cleaned_data["tasks"] = tasks

    sessions = data.get("sessions", [])
    if isinstance(sessions, list):
        cleaned_data["sessions"] = sessions

    next_task_id = data.get("next_task_id")
    if isinstance(next_task_id, int) and next_task_id > 0:
        cleaned_data["next_task_id"] = next_task_id
    else:
        cleaned_data["next_task_id"] = next_record_id(cleaned_data["tasks"])

    next_session_id = data.get("next_session_id")
    if isinstance(next_session_id, int) and next_session_id > 0:
        cleaned_data["next_session_id"] = next_session_id
    else:
        cleaned_data["next_session_id"] = next_record_id(cleaned_data["sessions"])

    cleaned_data["next_task_id"] = max(
        cleaned_data["next_task_id"], next_record_id(cleaned_data["tasks"])
    )
    cleaned_data["next_session_id"] = max(
        cleaned_data["next_session_id"],
        next_record_id(cleaned_data["sessions"]),
    )

    return cleaned_data


def load_data(file_path):
    path = Path(file_path)

    if not path.exists():
        return (
            create_app_data(),
            f"No existing data file found. Starting with a fresh StudyPilot file named {path.name}.",
        )

    try:
        with path.open("r", encoding="utf-8") as data_file:
            data = json.load(data_file)
    except json.JSONDecodeError:
        return (
            create_app_data(),
            "The JSON data file could not be read. StudyPilot is starting with empty data.",
        )
    except OSError as error:
        return create_app_data(), f"The data file could not be opened: {error}"

    return normalize_data(data), f"Loaded data from {path.name}."


def save_data(file_path, data):
    path = Path(file_path)
    cleaned_data = normalize_data(data)

    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8") as data_file:
            json.dump(cleaned_data, data_file, indent=2)
    except OSError as error:
        return False, f"StudyPilot could not save the JSON data file: {error}"

    return True, f"Saved data to {path.name}."
