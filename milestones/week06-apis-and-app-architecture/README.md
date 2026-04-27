# StudyPilot Week 6 - APIs And App Architecture

This milestone re-expresses StudyPilot through separated file responsibilities.

It demonstrates:

* visible application structure across multiple files
* task and session data shapes in `models.py`
* app logic in `services.py`
* JSON save and load behavior in `storage.py`
* output shaping and JSON-style response display in `views.py`
* app coordination in `main.py`

## Run It

From the repository root:

```bash
python milestones/week06-apis-and-app-architecture/main.py
```

## What It Includes

The program:

* loads saved Week 6 JSON data if it exists
* seeds sample tasks and sessions if the folder is starting fresh
* displays tasks, sessions, and a simple summary through separate view helpers
* saves data through a separate storage layer
* shows simulated JSON responses for `GET /api/tasks` and `GET /api/summary`

This is a recognition milestone, not a real framework or API server.

## What It Intentionally Omits

This Week 6 version does not include:

* a real web framework
* live HTTP endpoints
* full Django implementation
* large external dependency setup
* broad feature expansion

## Milestone Difference Note

Previous milestone:

Week 5 focused on JSON file persistence and beginner-readable error handling.

Next milestone:

Week 7 shifts from implementation snapshots toward project framing, constraints, and RBA-style decision explanation.

## Related Note

See ARCHITECTURE_NOTE.md for a short explanation of how the Week 6 file roles preview later application structure.

See WEEK05_TO_WEEK06_COMPARISON.md for a short instructional comparison of what changed from Week 5 to Week 6, why it changed, and what is still intentionally absent.

