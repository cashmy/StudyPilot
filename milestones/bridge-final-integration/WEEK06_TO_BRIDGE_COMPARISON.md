# StudyPilot Week 6 To Bridge Comparison

This note compares the Week 6 architecture milestone and the bridge-final-integration milestone in instructional terms.

Comparison context:

* earlier version: milestones/week06-apis-and-app-architecture
* later version: milestones/bridge-final-integration
* context: milestone-to-milestone transition

## 1. Short Summary Of The Overall Difference

Week 6 teaches structure.

The bridge milestone teaches integration.

Week 6 shows how StudyPilot can be separated into roles such as models, services, storage, views, and a coordinating main file. The bridge milestone then turns that structural preview into a fuller console experience that a learner can actually use through repeated menu-driven interaction.

## 2. What Was Added

The bridge milestone adds several behavioral pieces that Week 6 intentionally does not carry as a full user workflow:

* real menu-driven interaction
* prompt-based task entry
* task completion flow
* study-session logging flow
* filtered task views for incomplete, due-soon, and overdue work
* readable session views with totals by course and topic
* progress summaries and simple recommendations
* persistent JSON behavior tied directly to ongoing console use

## 3. What Was Reorganized Or Improved

The bridge milestone does not mainly introduce a new architecture idea.

Instead, it improves Week 6 by making the existing StudyPilot concepts feel behaviorally connected.

In Week 6, the learner recognizes application structure and simulated endpoint-style output.

In the bridge milestone, the learner sees those underlying ideas support a more complete planner workflow with clear user actions and stored results across runs.

## 4. What Is Still Intentionally Missing

The bridge milestone is still not the final console app.

It intentionally leaves some items for the final version, including:

* task removal flow
* explicit reload-from-file flow
* fuller menu completeness
* final wording and output polish
* the fully authoritative final behavior set

It also still avoids framework-heavy expansion, because that remains outside the core course boundary.

## 5. Why This Version Is Appropriate In The Sequence

This bridge milestone is appropriate because it closes the largest remaining jump after Week 6 without pretending that the final console version appears all at once.

* new concept added: multi-step console integration with fuller user workflows
* refinement of prior concept: Week 6 structure becomes more behaviorally usable and coherent
* concept still intentionally absent: the final polish and complete behavior set remain reserved for the canonical final console app

This makes the milestone sequence easier to explain.

Week 6 still teaches architecture recognition, the bridge teaches behavioral integration, and the final console version then serves as the polished plain-Python reference.
