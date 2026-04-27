# StudyPilot Week 4 - Debugging, Testing, And Structure

This milestone keeps the Week 3 function-based structure, but uses it to demonstrate debugging and code inspection.

It demonstrates:

* a broken calculation scenario that can be tested
* expected-versus-actual checks
* print-debugging to inspect why the result is wrong
* a corrected version of the same calculation
* a very small pytest-style recognition file

## Run It

From the repository root:

```bash
python milestones/week04-debugging-testing-structure/main.py
```

## What It Includes

The program:

* builds a small fixed set of study tasks
* runs a buggy summary calculation
* compares expected values to actual values
* prints debugging clues for each task
* runs the corrected summary calculation

The folder also includes `test_main.py` as a small pytest-style recognition example.

## Pytest Note

`test_main.py` is meant to be run with `pytest`.

If you run `python test_main.py`, you may see no test result output because the file defines test functions, but it does not call them directly.

## Install Pytest

From the repository root:

```bash
python -m pip install pytest
```

If you want to use the workspace virtual environment directly on Windows:

```bash
d:/@Coding_Projects/Python/StudyPilot/.venv/Scripts/python.exe -m pip install pytest
```

## Run The Tests

From the repository root:

```bash
python -m pytest milestones/week04-debugging-testing-structure/test_main.py -q
```

If you are already inside the Week 4 folder:

```bash
python -m pytest test_main.py -q
```

Useful options:

* `-q` shows a short result such as `2 passed`
* `-v` shows more detail about each test name
* `-s` allows `print()` output to appear while tests run

## What It Intentionally Omits

This Week 4 version does not include:

* file saving
* APIs
* framework-style separation
* heavy class-based design

It stays mostly function-based so the main lesson remains debugging and code literacy.

## Milestone Difference Note

Previous milestone:

Week 3 organized the StudyPilot logic into named functions and simple collections.

Next milestone:

Week 5 adds file persistence so the program can save and load structured task data instead of starting fresh each time.

## Related Note

See WEEK03_TO_WEEK04_COMPARISON.md for a short instructional comparison of what changed from Week 3 to Week 4, why it changed, and what is still intentionally absent.