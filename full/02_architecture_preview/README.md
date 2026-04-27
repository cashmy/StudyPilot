# StudyPilot Architecture Preview

This folder contains the architecture-preview version of StudyPilot.

It preserves the same core behavior as the console version, but separates the app into smaller files so the structure is easier to inspect and explain.

## Run It

From the repository root, run:

```bash
python full/02_architecture_preview/main.py
```

If you want to use the workspace virtual environment directly on Windows, run:

```bash
d:/@Coding_Projects/Python/StudyPilot/.venv/Scripts/python.exe full/02_architecture_preview/main.py
```

## Files

* `models.py` - study task and study session record shapes
* `services.py` - due checks, summaries, totals, and recommendations
* `storage.py` - JSON save and load behavior
* `views.py` - console display helpers
* `main.py` - prompts, menu flow, and app coordination
* `ARCHITECTURE_OVERVIEW.md` - short explanation of where each responsibility lives
* `WEEK6_INSTRUCTOR_COMPARISON.md` - short teaching note comparing this version to the console version
* `DJANGO_RECOGNITION_MAP.md` - simple recognition bridge from this structure to later Django ideas
* `../03_django_preview/WEEK6_AND_BEYOND_COMPARISON.md` - short side-by-side comparison of the console, architecture-preview, and Django versions

The app saves its data to `studypilot_data.json` in this same folder.