# StudyPilot Reference And Design Guide

This note gathers the main StudyPilot reference surfaces into one inspection point.

## Curated Reference Set

### Final Console Version

Reference path:

* `full/01_console_app`

Why it matters:

* this is the canonical behavioral version
* it keeps the project practical and runnable with standard Python
* it shows the full plain-Python StudyPilot direction

### Architecture Preview

Reference path:

* `full/02_architecture_preview`

Why it matters:

* it preserves the same core behavior
* it makes data, logic, storage, display, and flow easier to inspect
* it previews later application structure without requiring a framework

### Django Preview

Reference path:

* `full/03_django_preview`

Why it matters:

* it acts as an instructor-facing recognition bridge
* it shows how the same project idea can map into models, forms, views, templates, URLs, and admin
* it remains intentionally narrower than the console version

### Weekly Milestones

Reference path:

* `milestones/`

Why they matter:

* they show one instructional layer at a time
* they keep the course alignment visible week by week
* they help explain how the project grows without jumping too far ahead

## Main Design Decisions

### Canonical Behavior First

The full console version was treated as the main behavioral anchor.

That choice matters because later previews and milestones can be derived from a stable reference instead of drifting independently.

### Structure Should Follow Curriculum Readiness

StudyPilot was allowed to grow in structure only when the milestone sequence was ready for that change.

That kept the project explainable for an introductory audience.

### Optional Previews Must Stay Optional

The architecture preview and Django preview were framed as recognition tools, not hidden student requirements.

That protected the instructional boundary of the course.

### Polish Should Increase Clarity

In StudyPilot, polish is not treated as extra decoration.

It is treated as clearer explanation, cleaner references, stronger validation evidence, and more defensible scope choices.

## Recommended Presentation Order

If this project is shown as a polished reference set, a useful order is:

1. explain the project intent and boundary
2. show the final console version as the canonical behavior
3. show the architecture preview as the structure-recognition step
4. optionally show the Django preview as an instructor-facing bridge
5. use the milestone set to explain how the project aligns with the course week by week

That order keeps the project coherent and easy to explain.
