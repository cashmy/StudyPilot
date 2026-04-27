# StudyPilot Project Brief

## Project Name

StudyPilot

## Project Purpose

StudyPilot is an instructor demonstration project for the Python Programming course.

It is designed to show how a practical study-planning tool can be built, refined, and re-expressed across multiple levels of Python application structure.

The project should support curriculum demonstration, not replace student assignments.

## Primary Audience

The primary audience is the instructor.

Secondary audiences include:

* students viewing selected snapshots during class
* future Codex or LLM sessions that need project continuity
* curriculum reviewers interested in how Python concepts are scaffolded

## Educational Role

StudyPilot should demonstrate how a project can evolve from simple Python mechanics into a more complete application.

It should model:

* clear naming
* readable code
* beginner-friendly logic
* incremental refinement
* debugging and testing habits
* structured thinking
* responsible AI-assisted development
* RBA-style project framing and refactoring

## Planned Full Versions

### 1. Console App

The console version should be fully runnable with standard Python and no required external dependencies.

It should include useful study-planning behaviors such as:

* adding study tasks or sessions
* viewing planned study work
* tracking estimated or completed time
* organizing tasks by course, topic, priority, or due date
* showing summaries or recommendations
* saving and loading data if appropriate

This version is the closest match to the introductory Python course.

### 2. Architecture Preview

The architecture preview should express the same project idea with separated responsibilities, such as:

* data models or data structures
* input shaping or form-style validation
* view/output formatting
* application/controller flow
* persistence or service utilities

This version should not require Django or another web framework.

Its purpose is to help students recognize application structure before encountering a full framework.

### 3. Django Preview

The Django preview is optional and instructor-facing.

It may demonstrate how the same project concept could map into:

* models
* views
* templates
* forms
* URLs
* settings and app structure

Students should not be required to build this version in the introductory course.

It serves as a recognition bridge to real-world Python web development.

## Non-Goals

StudyPilot is not intended to be:

* a required student capstone
* a replacement for short targeted assignments
* a production SaaS product
* a complex Django course hidden inside an introductory Python course
* an AI-generated artifact with no human governance

## Development Guidance

When building StudyPilot, prioritize:

* clarity over cleverness
* explainability over abstraction
* useful behavior over feature count
* course alignment over architectural novelty
* intentional refactoring over uncontrolled expansion

The final versions should be created first, then earlier milestones should be derived from them.

This supports stable instructional alignment and reduces drift.
