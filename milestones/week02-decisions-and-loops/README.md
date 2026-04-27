# StudyPilot Week 2 - Decisions And Loops

This milestone extends the Week 1 snapshot into a small repeated-processing example.

It demonstrates:

* conditionals with `if` and `else`
* comparisons such as checking for `high` priority
* loop behavior with a fixed set of study tasks
* repeated output and a simple weekly-goal check

## Run It

From the repository root:

```bash
python milestones/week02-decisions-and-loops/main.py
```

## What It Includes

The program uses a small fixed collection of study tasks.

It loops through them and:

* prints each task
* checks whether the task is high priority
* checks whether the task is completed
* adds completed minutes to a running total
* reports whether the weekly study goal was met

## What It Intentionally Omits

This Week 2 version does not include:

* input prompts
* functions as the main structure
* file saving
* multi-file structure
* advanced input handling
* APIs

## Milestone Difference Note

Previous milestone:

Week 1 printed one fixed study summary with assigned variables and one simple expression.

Next milestone:

Week 3 adds functions and collections more intentionally so repeated logic can move into named parts and state can be managed more clearly.

## Related Note

See `WEEK01_TO_WEEK02_COMPARISON.md` for a short instructional comparison of what changed from Week 1 to Week 2, why it changed, and what is still intentionally absent.