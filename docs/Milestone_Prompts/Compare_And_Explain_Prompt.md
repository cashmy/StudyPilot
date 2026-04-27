# StudyPilot Compare and Explain Prompt

Use this prompt when you want the LLM to compare two StudyPilot milestone versions and explain what changed, why it changed, and what is still intentionally absent.

This prompt is especially useful for:

* instructor notes
* milestone transition summaries
* student-facing comparison explanations
* internal validation of curriculum alignment

It is derived from:

* `docs/StudyPilot_Curriculum_Alignment.md`

and should support that artifact, not override it.

---

## Prompt

```text
Read these files first and treat them as governing context:

1. D:\@Coding_Projects\Python\StudyPilot\docs\StudyPilot_Project_Brief.md
2. D:\@Coding_Projects\Python\StudyPilot\docs\StudyPilot_Curriculum_Alignment.md
3. D:\@Coding_Projects\Python\StudyPilot\docs\StudyPilot_Functional_Scope.md
4. D:\@Artifact_Generation\108_AAISE_Details\RBA_Canonical_Short_Definition.md

Comparison task:
- Earlier version: [ABSOLUTE PATH]
- Later version: [ABSOLUTE PATH]
- Comparison context: [WEEK-TO-WEEK / VERSION-TO-VERSION / MILESTONE-TO-FINAL]

Purpose:
- compare the two StudyPilot versions in instructional terms
- identify what changed structurally or behaviorally
- explain why those changes fit the curriculum progression
- identify what still remains intentionally absent

Instructions:
- focus on instructional and conceptual differences first
- do not write a code diff
- keep the explanation readable for an instructor or introductory student audience
- distinguish clearly between:
  - new concept added
  - refinement of prior concept
  - concept still intentionally absent

Output format:
1. short summary of the overall difference
2. what was added
3. what was reorganized or improved
4. what is still intentionally missing
5. why this version is appropriate for its place in the milestone sequence

If useful, mention:
- readiness alignment
- why certain later features were not introduced yet
- how this version prepares for the next milestone

Do not rewrite the code unless explicitly asked.
```

---

## Use Note

This prompt is best used after a milestone is created so the LLM can explain:

* what changed
* what the change teaches
* why the version remains bounded

That makes it a useful governance and instructional support artifact.
