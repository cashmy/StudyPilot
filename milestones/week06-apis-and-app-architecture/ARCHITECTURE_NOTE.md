# Week 6 Architecture Note

This Week 6 snapshot is meant to make file roles easy to inspect.

## File Roles

* `models.py` holds the task and session data shapes.
* `services.py` holds the logic that adds records, builds summaries, and prepares JSON-style payloads.
* `storage.py` holds the JSON save and load behavior.
* `views.py` holds display formatting and output shaping.
* `main.py` coordinates the overall flow.

## Why This Matters

The earlier milestones kept more responsibility in one file so the concept boundary stayed smaller.

Week 6 makes the structure more visible so students can recognize that:

* data can live in one place
* logic can live in another place
* save and load behavior can be isolated
* output can be shaped separately from the core logic
* the program flow can coordinate those parts

## MVT And Form Recognition Preview

This is not Django, but it previews later framework ideas:

* `models.py` previews model-style data definitions
* the shaped task and session input dictionaries in `main.py` preview form-style input
* `views.py` previews view/output responsibility

The goal is recognition, not framework mastery.