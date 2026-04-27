# StudyPilot Functional Scope

## Purpose

This artifact defines the practical functional scope of StudyPilot before development begins.

Its purpose is to reduce drift by clarifying:

* the core use case
* the main data objects
* the must-have behaviors
* the boundaries of the full console version
* what should remain out of scope for the introductory Python course

StudyPilot is both:

* an instructor continuity project
* a small, realistic, student-useful planning tool

The primary bias should remain:

* useful enough to feel real
* simple enough to stay teachable

---

## Core Use Case

StudyPilot is a:

* **study task and study session planner**

It helps a student:

* keep track of study tasks
* associate tasks with a course or topic
* log study time
* identify upcoming work
* view simple progress summaries

This combines:

* planning
* tracking
* lightweight decision support

without becoming a full productivity platform.

---

## Primary Design Goal

StudyPilot should feel like:

* a practical console utility that a student could actually imagine using

not:

* an overbuilt showcase app
* a disguised web framework project
* an AI gimmick

---

## Core Data Objects

The primary objects should remain minimal.

### 1. StudyTask

Represents planned work.

Suggested fields:

* `id`
* `course_name`
* `topic`
* `task_name`
* `priority`
* `due_date`
* `estimated_minutes`
* `completed`

---

### 2. StudySession

Represents time spent studying.

Suggested fields:

* `id`
* `course_name`
* `topic`
* `minutes_studied`
* `session_date`
* `notes`

---

### 3. Course

Optional for later structure only.

Suggested use:

* a lightweight grouping concept

Suggested fields if included:

* `course_name`
* `target_minutes_per_week`

This should remain optional in the console version and can be treated as a simple string first.

---

## Must-Have Behaviors

The full console version should support these baseline behaviors.

### Task Management

* add a study task
* view all study tasks
* view incomplete tasks
* mark a task as completed
* optionally remove or archive a task

---

### Session Logging

* log a study session
* view study sessions
* total minutes studied
* total minutes by course
* total minutes by topic

---

### Planning / Summary

* view tasks due soon
* view overdue tasks
* view simple weekly study summary
* compare estimated work against completed work in a simple way

---

### Recommendation / Guidance

Keep this rule-based, not AI-driven.

Examples:

* "You have 2 overdue tasks."
* "Math has the fewest study minutes this week."
* "Prioritize tasks due within 2 days."
* "You met your study target for one course but not another."

This should be framed as:

* simple program logic

not as:

* machine intelligence

---

## Input Style by Version

### Early Milestones

Use:

* hard-coded values
* direct variable assignment
* fixed collections

Reason:

* this keeps the project aligned with early-week course concepts

---

### Full Console Version

Use:

* menu-driven input
* simple numbered options
* plain console prompts

Reason:

* this makes the final console app actually usable without adding UI complexity

---

## Persistence Strategy

### Primary Save Format

Use:

* `JSON`

Reason:

* it matches course goals
* it is readable
* it supports structured data naturally
* it maps well to later architecture preview

---

### Optional Secondary Format

May include:

* `CSV` export or reporting

Reason:

* useful for demonstrations
* helpful for Week 5/6 comparison

But this should not become the primary storage format.

---

## Date Handling Strategy

### Early Milestones

Use:

* plain text due dates

Reason:

* avoids premature complexity

---

### Later / Full Version

Use:

* controlled `datetime` handling where it improves due-soon or overdue logic

Reason:

* realistic enough for the final version
* still explainable

---

## Architecture Preview Boundary

The architecture preview should separate responsibilities without pretending to be a framework.

Recommended file roles:

* `models.py`
* `services.py`
* `storage.py`
* `views.py`
* `main.py`

Possible interpretations:

* `models.py`:
  data objects or structured records
* `services.py`:
  business logic, summaries, recommendations
* `storage.py`:
  save/load behavior
* `views.py`:
  display formatting and output shaping
* `main.py`:
  user flow and menu control

This should support recognition of application structure without drifting into heavy framework conventions.

---

## Django Preview Boundary

The Django preview should remain:

* optional
* instructor-facing
* recognition-oriented

It may demonstrate:

* models
* views
* templates
* forms
* URL flow

It should **not** become:

* a hidden student requirement
* a full second implementation target

---

## Out of Scope

The StudyPilot project should stay out of these areas for the introductory Python course:

* authentication
* accounts or multi-user support
* database setup
* cloud sync
* notifications
* calendar integrations
* complex analytics
* large AI features
* framework-heavy implementation burden
* production-grade architecture ceremony

These may be discussable later, but they are not part of the intended scope now.

---

## Recommended Functional Center

If scope pressure appears during development, protect these first:

* task tracking
* session logging
* due-date visibility
* progress summary
* JSON persistence

If something must be cut, cut:

* optional export
* extra filtering
* extra recommendation rules
* optional course-level targeting features

---

## Final Scope Statement

StudyPilot should be developed as a **small but believable study-planning console application** that supports tasks, logged study time, basic summaries, and JSON persistence, with later re-expression into a cleaner architecture-preview form and an optional Django recognition example.

That scope is large enough to feel meaningful and small enough to remain aligned with the introductory Python course.
