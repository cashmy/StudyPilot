# Django Recognition Map

This note does not turn StudyPilot into Django.

Its purpose is to help instructors and students recognize how this architecture-preview version can prepare them for later Django or MVT-style thinking.

## Simple Recognition Bridge

* `models.py` is the closest preview of Django models.
  It defines the shape of the data the app works with.

* `services.py` is the closest preview of business logic that might later live beside or around Django models, forms, or utility modules.
  It answers questions like how work is sorted, summarized, or recommended.

* `storage.py` is a loose preview of persistence responsibility.
  In Django, database-backed models would replace most of this JSON file handling.

* `views.py` is not a Django view in the strict framework sense.
  In this version, it is closer to presentation and output formatting.
  It helps students notice that display concerns can be separated from logic before they later encounter Django views and templates.

* `main.py` is the clearest preview of application-flow coordination.
  In Django, URL routing, forms, and view functions would take over much of this interaction flow.

## Later Django Recognition Examples

If StudyPilot were later re-expressed in Django, students could recognize these likely moves:

* task and session record shapes would move toward Django model classes
* console prompts would move toward forms and submitted request data
* printed output would move toward templates
* menu flow would move toward URL patterns and view functions
* JSON file persistence would move toward the database layer

## Important Boundary

This architecture-preview version is still a small plain-Python console app.

It is useful because it gives students a bridge to later framework ideas without forcing framework complexity into the introductory course.
