# StudyPilot Week 5 - Files And Persistence

This milestone shifts StudyPilot toward file-based persistence.

It demonstrates:

* saving study tasks to a JSON file
* loading study tasks from a JSON file
* handling a missing file in a beginner-readable way
* handling invalid JSON data in a beginner-readable way

## Run It

From the repository root:

```bash
python milestones/week05-files-and-persistence/main.py
```

## What It Includes

The program:

* starts with a small fixed set of study tasks
* saves those tasks to `study_tasks.json`
* loads the saved tasks back from `study_tasks.json`
* tries to load a missing file to show simple missing-file handling
* creates `broken_study_tasks.json` to show simple invalid-file handling

The file behavior is direct and visible so students can inspect what JSON persistence is doing.

## What It Intentionally Omits

This Week 5 version does not include:

* API calls
* architecture-preview file splitting
* Django concepts
* advanced persistence patterns

## Milestone Difference Note

Previous milestone:

Week 4 focused on debugging, expected-versus-actual checks, and test recognition.

Next milestone:

Week 6 keeps the core StudyPilot behavior but starts previewing application structure, separated responsibilities, and architecture recognition.

## Related Note

See WEEK04_TO_WEEK05_COMPARISON.md for a short instructional comparison of what changed from Week 4 to Week 5, why it changed, and what is still intentionally absent.