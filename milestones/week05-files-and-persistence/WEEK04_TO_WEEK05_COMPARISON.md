# StudyPilot Week 4 To Week 5 Comparison

This note compares the Week 4 and Week 5 StudyPilot milestones in instructional terms.

Comparison context:

* earlier version: milestones/week04-debugging-testing-structure
* later version: milestones/week05-files-and-persistence
* context: week-to-week milestone progression

## 1. Short Summary Of The Overall Difference

Week 4 focuses on checking whether StudyPilot logic is correct through debugging, expected-versus-actual comparisons, and test recognition.

Week 5 keeps the program small, but shifts the main lesson toward file persistence.

The instructional change is from inspecting code behavior in memory to saving and loading structured task data from a JSON file.

## 2. What Was Added

Week 5 adds these new ideas:

* writing structured study-task data to a JSON file
* reading structured study-task data back from a JSON file
* checking whether a file exists before loading it
* handling invalid JSON data in a beginner-readable way
* validating that loaded data still matches the expected task structure

## 3. What Was Reorganized Or Improved

Week 5 improves the StudyPilot snapshot by making the task data survive outside the running program.

Instead of only building sample tasks in memory, the program now shows how those tasks can be stored, read back, and checked for basic file problems.

This is a refinement of the StudyPilot idea rather than a new product direction.

## 4. What Is Still Intentionally Missing

Week 5 still keeps several later concepts out of scope:

* API calls
* architecture-preview file splitting
* Django concepts
* advanced persistence patterns
* larger application structure

Those concepts are still intentionally missing so the main lesson stays on JSON files, save/load behavior, and simple error handling.

## 5. Why This Version Is Appropriate For Its Place In The Sequence

Week 5 is appropriate because it adds a realistic next step after debugging and testing.

* new concept added: file persistence with JSON plus simple missing-file and invalid-file handling
* refinement of prior concept: the same StudyPilot task data is now checked not only in memory, but also when it is saved and loaded
* concept still intentionally absent: broader architecture, APIs, and framework ideas remain for the next milestone

This matches student readiness well.

After students have seen how to inspect correctness in Week 4, Week 5 gives them a clear reason to care about structured data and file handling before StudyPilot expands into architecture recognition in Week 6.
