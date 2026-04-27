# StudyPilot Console App

This folder contains the final plain-Python console version of StudyPilot.

## Run It

From the repository root, run:

```bash
python full/01_console_app/main.py
```

If you want to use the workspace virtual environment directly on Windows, run:

```bash
d:/@Coding_Projects/Python/StudyPilot/.venv/Scripts/python.exe full/01_console_app/main.py
```

## What It Does

StudyPilot supports:

* study task management
* study session logging
* due-soon and overdue visibility
* rolling last-7-days summaries
* simple rule-based recommendations
* JSON save and load behavior

The app saves its data to `studypilot_data.json` in this same folder.

## Files

* `main.py` - menu flow and user interaction
* `logic.py` - summaries, due-date checks, and recommendations
* `storage.py` - JSON save and load behavior