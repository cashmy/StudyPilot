# Week 6 Instructor Comparison

This note is for instructional use.

It compares the final console version and the architecture-preview version of StudyPilot.

## What Stays The Same

Behavior stays the same in both versions:

* add study tasks
* view all, incomplete, due-soon, and overdue tasks
* mark tasks completed
* remove tasks
* log study sessions
* view study sessions and minute totals
* show rolling last-7-days summaries
* show simple rule-based recommendations
* save and load JSON data

This is the same app, not a new product and not a feature expansion.

## What Changes Structurally

The console version keeps most responsibilities close together.

That makes it easy to read from top to bottom, which fits earlier course weeks well.

The architecture-preview version separates those responsibilities into clearer files:

* `models.py` for record shapes
* `services.py` for app logic
* `storage.py` for JSON persistence
* `views.py` for printed output
* `main.py` for menu flow and coordination

## Why This Helps In Week 6

This version supports architecture recognition without requiring a framework.

Students can see that a program can separate:

* data
* logic
* storage
* display
* flow

That recognition matters before students encounter ideas like web frameworks, forms, templates, or model-view separation.

## Teaching Angle

The console version is good for asking, "How does the program work?"

The architecture-preview version is good for asking, "Where does each kind of work live?"

That is the main instructional shift.

## Suggested In-Class Prompts

* Which file decides how due-soon and overdue work is calculated?
* Which file changes if we only want to alter printed output?
* Which file changes if we only want to alter save and load behavior?
* Which file acts like the traffic controller for the whole app?
* What stayed behaviorally the same even after the structure changed?