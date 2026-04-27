import json
from pathlib import Path

from models import create_app_state


def normalize_app_state(data):
    clean_state = create_app_state()

    if not isinstance(data, dict):
        return clean_state

    tasks = data.get("tasks", [])
    if isinstance(tasks, list):
        clean_state["tasks"] = tasks

    sessions = data.get("sessions", [])
    if isinstance(sessions, list):
        clean_state["sessions"] = sessions

    return clean_state


def load_app_state(file_path):
    path = Path(file_path)

    if not path.exists():
        return create_app_state(), (
            f"No saved Week 6 JSON file was found. StudyPilot will start with sample architecture-preview data in {path.name}."
        )

    try:
        with path.open("r", encoding="utf-8") as file:
            loaded_data = json.load(file)
    except json.JSONDecodeError:
        return create_app_state(), (
            f"{path.name} contains invalid JSON. StudyPilot will continue with empty in-memory data."
        )
    except OSError as error:
        return create_app_state(), f"The data file could not be opened: {error}"

    return normalize_app_state(loaded_data), f"Loaded Week 6 data from {path.name}."


def save_app_state(file_path, app_state):
    path = Path(file_path)

    try:
        with path.open("w", encoding="utf-8") as file:
            json.dump(normalize_app_state(app_state), file, indent=2)
    except OSError as error:
        return False, f"StudyPilot could not save the Week 6 JSON file: {error}"

    return True, f"Saved Week 6 data to {path.name}."
