# StudyPilot Architecture Preview Prompt

Read these files first and treat them as governing context:

1. D:\@Coding_Projects\Python\StudyPilot\docs\StudyPilot_Project_Brief.md
2. D:\@Coding_Projects\Python\StudyPilot\docs\StudyPilot_Curriculum_Alignment.md
3. D:\@Coding_Projects\Python\StudyPilot\docs\StudyPilot_Functional_Scope.md
4. D:\@Artifact_Generation\108_AAISE_Details\RBA_Canonical_Short_Definition.md

Important context:
The full console version of StudyPilot is already complete.
This task is not to invent a new app or expand the feature set.
This task is to create the Architecture Preview version as a structural re-expression of the same core StudyPilot behavior.

Task:
Build the full Architecture Preview version of StudyPilot.

Purpose:
- preserve the same core behavior and scope as the console app
- reorganize the app into separated responsibilities
- make the structure easier to inspect and explain
- support Week 6 architecture recognition and later Django/MVT preview thinking
- remain beginner-readable and aligned to the introductory Python course

Constraints:
- do not add major new features
- do not turn this into a framework-style project
- do not start the Django preview
- prioritize clarity over abstraction
- preserve the instructional purpose
- keep the code small, readable, and explainable
- use JSON as the persistence format if persistence remains in scope
- avoid classes unless they clearly improve readability and structural teaching value

Recommended responsibility split:
- models.py
- services.py
- storage.py
- views.py
- main.py

Interpretation guidance:
- models.py: structured data objects or records
- services.py: business logic, summaries, due checks, and recommendations
- storage.py: save/load behavior
- views.py: output formatting and display helpers
- main.py: menu flow and app coordination

Deliverables:
- implement the architecture-preview code version
- include a short README for how to run it
- create a short companion explanation artifact describing where data, logic, storage, display, and flow live in this version
- briefly explain how this version differs from the console version structurally, not behaviorally

Start by summarizing:
1. the preserved feature set from the console version
2. the proposed file structure
3. any meaningful ambiguities

If any meaningful ambiguity remains, ask clarifying questions before implementation. After answers and approval, implement the architecture preview.
