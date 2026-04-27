# StudyPilot Django Preview

This folder contains the optional Django preview version of StudyPilot.

It is instructor-facing and recognition-oriented. The goal is to show how the same StudyPilot idea can map into Django models, forms, views, templates, URLs, and admin without turning the project into a large web app.

## Setup

From the repository root:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install Django
cd full/03_django_preview
python manage.py migrate
```

## Run

From `full/03_django_preview`:

```bash
python manage.py runserver
```

Then open `http://127.0.0.1:8000/`.

## Optional Admin Setup

To use Django admin:

```bash
python manage.py createsuperuser
```

Then open `http://127.0.0.1:8000/admin/`.

## What This Preview Includes

* dashboard home page
* task list
* add task form
* mark task complete action
* study session log form
* session list page
* simple progress summary on the dashboard
* due soon and overdue indicators
* Django admin for `StudyTask` and `StudySession`

## Files To Inspect

* `planner/models.py` - data models
* `planner/forms.py` - form handling
* `planner/views.py` - function-based views and page logic
* `planner/urls.py` - app URL routing
* `planner/templates/planner/` - HTML templates
* `planner/admin.py` - admin registration
* `DJANGO_PREVIEW_OVERVIEW.md` - short explanation of where each responsibility lives
* `Instructor_Use_Notes-Django_Preview.md` - longer instructor-facing teaching note for the Django walkthrough
* `WEEK6_AND_BEYOND_COMPARISON.md` - short side-by-side comparison of the console, architecture-preview, and Django versions