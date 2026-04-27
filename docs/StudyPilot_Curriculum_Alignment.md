# StudyPilot Curriculum Alignment

## Purpose

This document connects the StudyPilot instructor demonstration project to the Python Programming course structure.

StudyPilot should support the course without becoming the course.

Students complete short targeted assignments. StudyPilot is the instructor continuity project that shows how the same concepts can accumulate into a larger useful tool.

## Course Alignment Principle

Each milestone should align with weekly course goals at a minimum.

Additional milestone versions may be added when a topic benefits from more than one snapshot, but the default structure should remain weekly so students can compare growth over time.

## Planned Milestone Map

### Week 1 - Basic Values

Focus:

* output
* variables
* strings
* numbers
* simple expressions
* possibly assigned values instead of input

StudyPilot snapshot:

* displays a simple study plan summary
* uses variables for course name, task name, time estimate, and due date text
* calculates a simple total or remaining minutes

Related student assignment:

* Assignment 1 - First Programs

### Week 2 - Decisions and Loops

Focus:

* conditionals
* comparisons
* loop behavior
* repeated output or repeated processing

StudyPilot snapshot:

* checks task priority or completion status
* loops through several study tasks
* reports whether weekly study goals are met

Related student assignments:

* Assignment 2 - Decisions in Code
* Assignment 3 - Loops and Repetition

### Week 3 - Functions and Collections

Focus:

* functions
* parameters
* return values
* lists and dictionaries
* simple state management

StudyPilot snapshot:

* stores study tasks in lists or dictionaries
* uses functions to add, display, summarize, and evaluate tasks
* separates repeated logic into named functions

Related student assignments:

* Assignment 4 - Function Builder
* Assignment 5 - List or Dictionary Mini-App

### Week 4 - Debugging, Testing, and Structure

Focus:

* debugging process
* print-debugging
* expected vs actual checks
* pytest recognition
* class-based structure recognition

StudyPilot snapshot:

* includes a broken or testable calculation scenario
* demonstrates evidence-based debugging
* adds simple tests or expected-vs-actual checks
* optionally compares function-based and class-based organization

Related student assignments:

* Assignment 6 - Debug and Explain
* Assignment 7 - Reading Structured Code

### Week 5 - Files and Persistence

Focus:

* text, CSV, or JSON files
* save/load behavior
* basic error handling
* structured data reading

StudyPilot snapshot:

* saves study tasks to a file
* loads saved tasks from a file
* handles missing or invalid file data in a beginner-readable way

Related student assignments:

* Assignment 8 - Save and Load Utility
* Assignment 9 - Structured Data Reader

### Week 6 - APIs and App Architecture

Focus:

* APIs and endpoints
* JSON responses
* Python beyond console scripts
* architecture recognition
* MVT/templates/forms preview

StudyPilot snapshot:

* optionally reads external or simulated external data
* separates application concerns into multiple files
* previews model/view/form-style organization without requiring Django
* may include a guided Django preview as instructor-only inspection

Related student assignments:

* Assignment 10 - Data Representation and App-Structure Preview
* Assignment 11 - API Data Fetcher
* Assignment 12 - Python App Architecture Preview

### Week 7 - RBA Project Framing

Focus:

* project intent
* constraints
* structure choices
* AI-assisted planning with accountability
* RBA mini-unit concepts

StudyPilot snapshot:

* includes project framing documentation
* shows how structure decisions were made
* identifies where AI could help and where human judgment governs
* connects StudyPilot development to RBA methodology

Related student assignments:

* Assignment 13 - RBA Project Framing Exercise
* Assignment 14 - Capstone Proposal and Approval

### Week 8 - Capstone-Style Polish

Focus:

* integration
* explanation
* testing and revision
* presentation
* AI use justification

StudyPilot snapshot:

* demonstrates a polished reference version
* includes explanation of design decisions
* includes testing or validation evidence
* includes an AI-use or RBA-process reflection if useful

Related student assignments:

* Assignment 15 - Capstone Build
* Assignment 16 - AI Use Justification and Final Presentation

## Governance Notes

StudyPilot should remain clearly separated from student assignments.

The project may inspire students, but it should not become a hidden requirement or a near-solution to their assignments.

Milestones should be instructional snapshots, not evidence that students are expected to build the same project.

## Suggested VS Code Codex Handoff Prompt

Use this prompt when beginning the StudyPilot build in a coding-focused Codex session:

```text
Read docs/StudyPilot_Project_Brief.md and docs/StudyPilot_Curriculum_Alignment.md first.
Preserve the instructional purpose.
Build the full console version first, then derive milestone snapshots from the final direction.
Keep code readable for an introductory Python course.
Do not optimize beyond student readability unless the brief explicitly calls for it.
Do not turn this into a required student project.
```
