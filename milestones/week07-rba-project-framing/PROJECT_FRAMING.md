# StudyPilot Project Framing

This document treats StudyPilot as a case object for Week 7 project framing.

## Project Intent

StudyPilot is an instructor demonstration project for an introductory Python course.

Its purpose is to show how the same practical planning tool can evolve across multiple levels of Python structure without becoming a hidden student requirement.

The project should support the course, not replace the course.

## Core Constraints

StudyPilot is governed by these main constraints:

* it must remain readable for an introductory Python audience
* it must align to the weekly milestone sequence
* it must stay separate from student assignments
* it should grow in structure only when the curriculum is ready for that shift
* it should avoid turning optional previews into implied student obligations

These constraints matter because they prevent the project from drifting into an overbuilt showcase app.

## Structure Choices

The project uses different structures at different points for instructional reasons.

### Final Console Version

The final console version is the canonical behavioral reference.

It keeps the core StudyPilot features practical and runnable with standard Python.

### Architecture Preview

The architecture preview keeps the same core behavior, but separates responsibilities so students can recognize application structure before seeing a web framework.

### Django Preview

The Django preview is optional and instructor-facing.

Its purpose is recognition, not a new required build target.

### Weekly Milestones

The milestone sequence deliberately changes one instructional layer at a time:

* Week 1 shows values and output
* Week 2 adds decisions and loops
* Week 3 adds functions and collections
* Week 4 adds debugging and test recognition
* Week 5 adds JSON files and persistence
* Week 6 adds architecture recognition

That structure keeps the project explainable and reduces concept overload.

## Why These Choices Were Made

These choices were made to preserve three things at once:

* curriculum alignment
* realistic project continuity
* manageable complexity

Without those constraints, StudyPilot could easily become a larger application than the course can support.

## Human Governance

Human judgment governs:

* what the project is for
* what each milestone is allowed to teach
* what must remain out of scope
* how far a preview is allowed to go
* whether a generated artifact stays aligned to the course

This is especially important when AI is used to help draft or refactor artifacts.

## Framing Outcome

The result is a project that stays useful enough to feel real, but bounded enough to remain teachable.

That is the main Week 7 framing lesson.
