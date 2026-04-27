# StudyPilot Week 3 To Week 4 Comparison

This note compares the Week 3 and Week 4 StudyPilot milestones in instructional terms.

Comparison context:

* earlier version: milestones/week03-functions-and-collections
* later version: milestones/week04-debugging-testing-structure
* context: week-to-week milestone progression

## 1. Short Summary Of The Overall Difference

Week 3 focuses on organizing StudyPilot into named functions and simple collections.

Week 4 keeps that function-based structure, but turns it into something students can inspect, debug, and test.

The main instructional shift is from writing organized code to examining whether organized code is actually correct.

## 2. What Was Added

Week 4 adds these new ideas:

* a buggy summary calculation that can be inspected
* expected-versus-actual checks
* print-debugging output to trace what the code is doing
* a corrected version of the same calculation
* a small pytest-style recognition example

## 3. What Was Reorganized Or Improved

Week 4 improves the StudyPilot snapshot by using the Week 3 function structure as a readable surface for debugging.

Instead of only separating responsibilities into functions, the program now uses that structure to compare results, spot a mistake, and confirm the fix.

This is a refinement of Week 3 rather than a feature expansion.

The StudyPilot idea remains small and familiar, but the code is now being read as evidence instead of only being run for output.

## 4. What Is Still Intentionally Missing

Week 4 still keeps several later concepts out of scope:

* file saving and loading
* APIs
* framework-style separation
* heavy class-based design
* larger application structure

Those concepts are intentionally still missing so the main lesson stays on debugging process, expected results, testing recognition, and code literacy.

## 5. Why This Version Is Appropriate For Its Place In The Sequence

Week 4 is appropriate because it builds directly on the structure introduced in Week 3.

* new concept added: debugging evidence, expected-versus-actual thinking, and pytest recognition
* refinement of prior concept: Week 3 functions are now used as parts that can be inspected and validated
* concept still intentionally absent: persistence and broader architecture are still saved for later milestones

This matches student readiness well.

Students first see how to organize code, then they see how to question that code and verify whether it behaves correctly.

That prepares them well for Week 5, where correct behavior will matter even more once task data is saved and loaded from files.
