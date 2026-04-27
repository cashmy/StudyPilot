# StudyPilot Django Preview Prompt

Read these files first and treat them as governing context:

1. D:\@Coding_Projects\Python\StudyPilot\docs\StudyPilot_Project_Brief.md
2. D:\@Coding_Projects\Python\StudyPilot\docs\StudyPilot_Curriculum_Alignment.md
3. D:\@Coding_Projects\Python\StudyPilot\docs\StudyPilot_Functional_Scope.md
4. D:\@Artifact_Generation\108_AAISE_Details\RBA_Canonical_Short_Definition.md

Important context:
The full console version and the architecture preview already exist or are being treated as prior versions.
This task is to build the optional Django Preview version of StudyPilot.

Purpose:
- demonstrate how the same StudyPilot concept maps into a real Django app
- show models, forms, views, templates, urls, and admin in a concrete way
- provide a believable UI/UX demo
- remain instructor-facing and recognition-oriented
- not become a hidden student requirement or a production-grade SaaS app

Constraints:
- use Django with the default SQLite database
- create a single app named planner
- keep the feature scope intentionally narrow
- do not try to replicate every console feature
- prioritize structural clarity over feature count
- keep the app easy to run locally
- keep the UI clean, simple, and readable
- avoid unnecessary frontend complexity
- preserve the same general StudyPilot concept, but reduce scope where helpful for demonstration

Recommended feature scope:
- dashboard / home page
- task list
- add task form
- mark task complete
- study session log form
- simple session summary
- due soon / overdue indicators
- basic progress summary
- Django admin for StudyTask and StudySession

Recommended Django structure:
- Django project root
- app: planner
- models.py
- forms.py
- views.py
- urls.py
- templates/planner/
- admin.py
- optional static styling if light and useful

Instructional guidance:
- optimize the Django version for instructional recognition and demonstration
- students should be able to inspect the app and understand, at a beginner level, where data lives, where input handling happens, where logic flow happens, and where presentation lives
- choose simpler patterns over more professional abstractions when simplicity improves explainability

Deliverables:
- implement the Django preview app
- include a README with setup and run instructions
- include a short explanation artifact describing:
  - where models live
  - where forms live
  - where views live
  - where templates live
  - where URL routing lives
  - how this version differs from the console app and architecture preview
- register the main models in Django admin
- use SQLite for simplicity

Start by summarizing:
1. the reduced feature set you propose for the Django preview
2. the Django file/app structure
3. any meaningful ambiguities

If any meaningful ambiguity remains, ask clarifying questions before implementation. After answers and approval, implement the Django preview.

Place the generated code in the folder: `full/03_django_preview/`