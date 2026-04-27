# StudyPilot Week 2 To Week 3 Comparison

This note compares the Week 2 and Week 3 StudyPilot milestones in instructional terms.

Comparison context:

* earlier version: `milestones/week02-decisions-and-loops`
* later version: `milestones/week03-functions-and-collections`
* context: week-to-week milestone progression

## 1. Short Summary Of The Overall Difference

Week 2 shows decisions and loops directly in one visible top-to-bottom flow.

Week 3 keeps the same general StudyPilot behavior, but reorganizes that behavior into named functions and clearer collection-based state.

The main instructional shift is from using logic directly to organizing that logic into reusable parts.

## 2. What Was Added

Week 3 adds these new ideas:

* named functions with clear jobs
* parameters used to send task data into functions
* return values used to send results back out
* a more intentional list-and-dictionary state model
* clearer separation between adding, displaying, evaluating, and summarizing tasks

## 3. What Was Reorganized Or Improved

Week 3 improves the StudyPilot snapshot by moving repeated logic out of the main flow and into helper functions.

That means the program is easier to read by responsibility:

* one function adds tasks
* one function displays tasks
* one function evaluates tasks
* one function summarizes the full set of tasks

This is a refinement of the Week 2 program rather than a new feature-heavy version.

## 4. What Is Still Intentionally Missing

Week 3 still keeps several later ideas out of scope:

* file saving and loading
* APIs
* multi-file application structure
* heavy class-based design
* advanced input handling

Those concepts are intentionally missing so the focus remains on functions, parameters, return values, and simple collection-based state.

## 5. Why This Version Is Appropriate For Its Place In The Sequence

Week 3 is appropriate because it adds the next layer of organization without making the project too large.

* new concept added: functions, parameters, return values, and more intentional collections
* refinement of prior concept: Week 2 loop-and-decision logic is preserved but reorganized into named parts
* concept still intentionally absent: persistence, broader architecture, and framework ideas remain for later milestones

This matches student readiness well.

It prepares students for Week 4 by making the code structured enough to inspect, debug, and test more deliberately.
