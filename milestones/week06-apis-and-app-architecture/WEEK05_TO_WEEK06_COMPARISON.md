# StudyPilot Week 5 To Week 6 Comparison

This note compares the Week 5 and Week 6 StudyPilot milestones in instructional terms.

Comparison context:

* earlier version: milestones/week05-files-and-persistence
* later version: milestones/week06-apis-and-app-architecture
* context: week-to-week milestone progression

## 1. Short Summary Of The Overall Difference

Week 5 focuses on saving and loading StudyPilot task data through a JSON file.

Week 6 keeps JSON persistence, but shifts the main lesson toward architecture recognition.

The instructional change is from file handling in one small program to seeing how the same app idea can be separated into visible responsibilities such as data, logic, storage, display, and coordination.

## 2. What Was Added

Week 6 adds these new ideas:

* separate files for models, services, storage, views, and main flow
* a clearer distinction between data shape, logic, storage, and output
* simulated JSON-style endpoint payloads
* a recognition bridge toward later model-view-form or framework thinking

## 3. What Was Reorganized Or Improved

Week 6 improves the StudyPilot snapshot by keeping the same core task and session idea while making the file roles easy to inspect.

Instead of having persistence and behavior demonstrated in one file, the program now spreads those responsibilities across named parts.

This is a structural refinement, not a broad feature expansion.

## 4. What Is Still Intentionally Missing

Week 6 still keeps several later ideas out of scope:

* a real web framework
* live HTTP endpoints
* full Django implementation
* large external dependency setup
* broad feature expansion

Those concepts are intentionally still missing so the main lesson stays on architecture recognition rather than framework mastery.

## 5. Why This Version Is Appropriate For Its Place In The Sequence

Week 6 is appropriate because it introduces a new level of structure without requiring students to learn a full framework.

* new concept added: separated responsibilities and JSON-style response thinking
* refinement of prior concept: Week 5 JSON persistence is preserved, but moved into a clearer storage role
* concept still intentionally absent: live APIs and framework implementation remain for optional later recognition work

This matches student readiness well.

After students understand variables, loops, functions, debugging, and JSON files, Week 6 gives them a readable preview of how a larger Python application can be organized.
