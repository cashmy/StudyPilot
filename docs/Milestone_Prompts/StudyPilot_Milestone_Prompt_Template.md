# StudyPilot Milestone Prompt Template

Use this template to generate or refine a StudyPilot milestone snapshot.

This prompt layer is **derived from** `docs/StudyPilot_Curriculum_Alignment.md`.

It should operationalize that artifact, not override it.

---

## Prompt

```text
Read these files first and treat them as governing context:

1. D:\@Coding_Projects\Python\StudyPilot\docs\StudyPilot_Project_Brief.md
2. D:\@Coding_Projects\Python\StudyPilot\docs\StudyPilot_Curriculum_Alignment.md
3. D:\@Coding_Projects\Python\StudyPilot\docs\StudyPilot_Functional_Scope.md
4. D:\@Artifact_Generation\108_AAISE_Details\RBA_Canonical_Short_Definition.md

Milestone target:
- [WEEK / FOLDER NAME]
- Output folder: [ABSOLUTE OUTPUT FOLDER]

Build source:
- [FROM SCRATCH / DERIVE FROM PREVIOUS MILESTONE / DERIVE FROM FINAL CONSOLE VERSION]
- If deriving, source path: [ABSOLUTE SOURCE PATH]

Instructional purpose:
- This milestone is an instructional snapshot, not a production app version.
- It must align to the weekly concept boundary in StudyPilot_Curriculum_Alignment.md.
- It must remain clearly separated from student assignments and should not become a near-solution to them.

Focus for this milestone:
- [FOCUS ITEMS]

Required behaviors:
- [REQUIRED BEHAVIORS]

Not yet allowed / intentionally absent:
- [NOT-YET CONCEPTS OR FEATURES]

Implementation guidance:
- Keep code readable for an introductory Python course.
- Prefer the smallest useful implementation that demonstrates the concept clearly.
- Do not add features that belong to later milestones.
- Do not optimize beyond student readability unless there is a strong instructional reason.
- If something from the final app is too advanced for this milestone, simplify or omit it.

Expected files:
- [FILES TO CREATE]

Deliverables:
- implement the milestone snapshot in the target folder
- include a short README explaining what this milestone demonstrates
- include a short note describing how this milestone differs from the previous and next milestone

Start by summarizing:
1. the concept boundary for this milestone
2. the behaviors you will include
3. the behaviors or structures you will intentionally omit
4. any meaningful ambiguity

If any meaningful ambiguity remains, ask clarifying questions before implementation. After answers and approval, implement the milestone.
```

---

## Use Note

Prefer:

* deriving from the final console version when rollback is simpler and cleaner

or:

* deriving from the previous milestone when continuity is more important than rollback simplicity

Choose the source that best preserves alignment and beginner readability.
