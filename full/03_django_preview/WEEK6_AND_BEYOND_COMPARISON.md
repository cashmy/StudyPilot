# Week 6 And Beyond Comparison

This note is for instructor use.

It places the three main StudyPilot reference versions side by side so the instructional shift stays clear.

## What Stays Stable

In all three versions, StudyPilot is still about the same core ideas:

* study tasks
* study sessions
* due dates and priority
* simple progress tracking
* a small, explainable tool rather than a large product

The project idea stays stable. The structure and delivery form change.

## Side-By-Side Map

| Version | Primary instructional purpose | Main structure | Input and output | Persistence |
| --- | --- | --- | --- | --- |
| Final console app | Show a complete plain-Python application in a readable menu-driven form | A light three-file split centered on menu flow, logic, and storage | Console prompts and printed summaries | JSON file |
| Architecture preview | Show separation of concerns without requiring a framework | Plain-Python split into data, logic, storage, display, and flow files | Console prompts and printed output, but with clearer file roles | JSON file |
| Django preview | Show how the same idea maps into a real web framework structure | Django models, forms, views, templates, URLs, and admin | Browser pages, HTML templates, form submissions, and admin screens | SQLite through Django ORM |

## What To Emphasize In Week 6

For Week 6, the architecture preview should usually do the main teaching work.

It shows app structure, file roles, and separation of concerns while staying inside plain Python.

The Django preview should remain a bounded recognition bridge.

It is useful for saying, "Here is where these same ideas can go next," not for starting a full framework unit.

## What To Emphasize In Weeks 7 And 8

In Week 7, these three versions can support project-framing discussion:

* why structure choices changed
* why the project did not need every possible feature
* where scope was intentionally reduced for teaching clarity

In Week 8, they can support reflection and polish discussion:

* the same project idea can appear in multiple legitimate forms
* cleaner structure is not the same thing as feature growth
* explanation and validation matter alongside implementation

## Short Framing Lines

Useful instructor phrasing:

* The app idea stayed the same while the organizational form changed.
* The architecture preview is the main Week 6 teaching version.
* The Django preview is a recognition bridge, not a new student requirement.