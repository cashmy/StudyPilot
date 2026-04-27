# Instructor Use Notes - Django Preview

## Purpose

This note supports instructor use of the StudyPilot Django Preview during class.

Its goal is not to turn the introductory Python course into a Django unit.

Its goal is to help the instructor use this version as a recognition bridge so students can see how the same StudyPilot concept can later appear in a real web application structure.

---

## Primary Teaching Goal

The main teaching goal is:

* help students recognize that Python can grow from a console program into a web application with separated responsibilities

This version should communicate:

* the project idea is still the same
* the structure is different
* the app now has a web interface
* the data is stored in a database instead of a JSON file
* forms, views, templates, and models each play a role

---

## What Students Should Notice

When showing the Django preview, direct attention to:

* the same StudyPilot concept still exists
* tasks and study sessions are now represented through Django models
* user input now happens through forms instead of console prompts
* output now appears through templates instead of printed text
* app flow now moves through URL routing and view functions rather than a console menu loop
* persistence now happens through Django and SQLite rather than manual JSON save/load

---

## Suggested Walkthrough Order

Use a short, bounded walkthrough.

### 1. Start with the UI

Show:

* dashboard
* task list
* add task form
* session log form

Suggested wording:

> "This is still StudyPilot. The difference is not the core idea. The difference is how the application is expressed."

---

### 2. Connect the UI to the Earlier Versions

Briefly remind students:

* console version:
  one app, menu-driven, JSON persistence
* architecture preview:
  same app with separated responsibilities
* Django preview:
  same idea expressed in a real web framework structure

Suggested wording:

> "The concept did not change. The organizational form changed."

---

### 3. Point Out the Main Django Parts

Show at a high level:

* `models.py`
* `forms.py`
* `views.py`
* `templates`
* `urls.py`
* `admin.py`

Use plain-language mappings:

* models = the data shape
* forms = how input is collected and validated
* views = how requests are handled
* templates = how information is displayed
* urls = how the app decides where requests go
* admin = a management interface for records

---

### 4. Keep the Framing Narrow

Students do **not** need to leave this session thinking:

* "I know Django now."

They should leave thinking:

* "I can see how Python can scale into a structured web app."

That is the right success target.

---

## What Not to Overemphasize

Avoid turning this walkthrough into:

* Django setup training
* deep framework theory
* deployment discussion
* production architecture discussion
* authentication, permissions, or scaling talk
* a hidden expectation that students must now build web apps

The preview should remain:

* concrete
* bounded
* confidence-building

---

## Best Framing Language

Helpful phrases:

* "This is the same project idea in a different architectural form."
* "We are recognizing structure, not mastering Django."
* "The concept is stable; the expression changed."
* "This helps you see where Python can go next."

Less helpful phrases:

* "Now we are learning Django."
* "This is the professional way, so the earlier version was only basic."
* "You will need to build this now."

---

## Why This Preview Is Valuable

This version has high value because it helps reduce the cognitive leap between:

* beginner console code
* structured Python code
* real framework-based application structure

Instead of making Django feel like a separate universe, this preview makes it feel like:

* a later expression of already recognizable ideas

That is the key pedagogical benefit.

---

## Suggested Time Use

Recommended use:

* `5-10` minute bounded walkthrough

This should be enough to:

* show the interface
* point out the major Django parts
* connect it to the earlier versions
* reinforce that recognition is the goal

---

## Final Reminder

The Django preview is a bridge, not a burden.

If students leave with:

* a clearer sense of how Python applications can evolve
* a lower sense of mystery around web application structure
* a stronger understanding that the same project idea can live in multiple forms

then the preview has done its job.
