# StudyPilot Django Preview Overview

This version is a reduced Django re-expression of StudyPilot.

It does not try to replicate every console feature. Its goal is to make Django structure easy to inspect.

## Where Each Responsibility Lives

* Models live in `planner/models.py`.
  This is where `StudyTask` and `StudySession` are defined.

* Forms live in `planner/forms.py`.
  This is where Django form handling for adding tasks and logging sessions is defined.

* Views live in `planner/views.py`.
  This is where the dashboard, list pages, add forms, and task-complete action are coordinated.

* Templates live in `planner/templates/planner/`.
  This is where the page layout and HTML presentation live.

* URL routing lives in `planner/urls.py` and `studypilot_site/urls.py`.
  The planner app routes page URLs, and the project routes those planner URLs into the site.

## How This Differs From Earlier Versions

The console app keeps nearly everything in one plain-Python menu-driven flow.

The architecture preview separates data, logic, storage, display, and flow into clearer plain-Python files.

The Django preview goes one step further by showing how the same general StudyPilot concept maps into framework structure:

* models for stored data
* forms for input handling
* views for request and page logic
* templates for presentation
* URL routing for page flow
* admin for inspection and basic data management

## Scope Boundary

This preview is intentionally narrower than the console app.

It keeps enough of StudyPilot to feel real, but trims scope so the Django structure stays easy to explain and easy to run locally.