# StudyPilot Week 3 - Functions And Collections

This milestone reorganizes the Week 2 snapshot so the repeated StudyPilot logic lives in named functions.

It demonstrates:

* functions with clear responsibilities
* parameters used to pass task data into functions
* return values used to send evaluation and summary results back
* lists and dictionaries for simple state management

## Run It

From the repository root:

```bash
python milestones/week03-functions-and-collections/main.py
```

## What It Includes

The program stores study tasks in a list of dictionaries.

It uses separate functions to:

* add tasks
* display tasks
* evaluate tasks
* summarize tasks

This keeps the logic more organized while still staying in one beginner-readable file.

## What It Intentionally Omits

This Week 3 version does not include:

* file saving
* APIs
* multi-module architecture
* heavy class-based design
* advanced input handling

## Milestone Difference Note

Previous milestone:

Week 2 showed decisions and loops directly in one visible flow.

Next milestone:

Week 4 adds debugging, expected-versus-actual checking, and code-reading support so students can inspect behavior more carefully and reason about mistakes.

## Related Note

See `WEEK02_TO_WEEK03_COMPARISON.md` for a short instructional comparison of what changed from Week 2 to Week 3, why it changed, and what is still intentionally absent.