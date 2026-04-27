# StudyPilot Architecture Overview

This version is the same StudyPilot app behaviorally as the console version.

The difference is structural: responsibilities are split into smaller files so the app is easier to inspect and explain.

## Plain-Language Map

* Data lives in `models.py`. This file shows the basic task, session, and app-data record shapes.
* Logic lives in `services.py`. This file handles sorting, due checks, summaries, totals, and simple recommendations.
* Storage lives in `storage.py`. This file loads and saves StudyPilot data in JSON format.
* Display lives in `views.py`. This file prints menus, task lists, session lists, totals, and summaries.
* Main application flow lives in `main.py`. This file handles prompts, menu choices, and calls the other files in the right order.

## Structural Difference From The Console Version

The console version keeps user interaction, output, logic, and storage closer together.

The architecture preview keeps the same behavior but separates those responsibilities so students can recognize how a small Python app can be organized before seeing a framework or Django-style structure.