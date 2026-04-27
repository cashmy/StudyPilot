# StudyPilot Bridge Final Integration Prompt

Use this prompt to create a code-bearing bridge milestone between:

* `week06-apis-and-app-architecture`

and:

* the final full console version

This bridge exists because Weeks 7 and 8 are primarily documentation-, framing-, validation-, and presentation-oriented in the curriculum.

That means they do not naturally carry the full technical integration load in code.

The purpose of this bridge milestone is to close the behavioral and structural gap honestly rather than pretending the final version appears without an intermediate integration step.

---

## Prompt

```text
Read these files first and treat them as governing context:

1. D:\@Coding_Projects\Python\StudyPilot\docs\StudyPilot_Project_Brief.md
2. D:\@Coding_Projects\Python\StudyPilot\docs\StudyPilot_Curriculum_Alignment.md
3. D:\@Coding_Projects\Python\StudyPilot\docs\StudyPilot_Functional_Scope.md
4. D:\@Artifact_Generation\108_AAISE_Details\RBA_Canonical_Short_Definition.md

Comparison sources:
- Earlier milestone: D:\@Coding_Projects\Python\StudyPilot\milestones\week06-apis-and-app-architecture
- Final console version: D:\@Coding_Projects\Python\StudyPilot\full\01_console_app

Target bridge output folder:
- [SET THE ABSOLUTE BRIDGE FOLDER PATH]

Purpose:
- create a code-bearing bridge milestone between Week 6 and the final console app
- preserve the honesty of the curriculum sequence
- show how the project becomes more behaviorally complete before the final polished version

Instructions:
- identify the meaningful behavioral gap between the Week 6 milestone and the final console version
- implement a milestone snapshot that closes most of that gap without simply duplicating the final version
- preserve beginner readability
- keep this version recognizably closer to the final app than Week 6 is
- do not add unrelated new features

What this bridge should usually include:
- integration of missing core behaviors that exist in the final console app
- improved flow coherence
- fuller summaries or recommendations if they are already part of the final app
- clearer app completeness than Week 6, but still not the final polished artifact

What this bridge should avoid:
- unnecessary new scope
- presentation-oriented polish as the main point
- replacing the final version
- pretending that Week 7 or Week 8 code work already solved the gap if they did not

Deliverables:
- implement the bridge milestone code snapshot
- include a short README explaining why this bridge milestone exists
- include a short note describing:
  - what gap it closes from Week 6
  - what still remains for the final version

Start by summarizing:
1. the major behavioral differences between Week 6 and the final version
2. what this bridge milestone will include
3. what it will still intentionally leave to the final version
4. any meaningful ambiguity

If any meaningful ambiguity remains, ask clarifying questions before implementation. After answers and approval, implement the bridge milestone.
```

---

## Naming Suggestion

Suggested folder names:

* `bridge-final-integration`
* `week06-to-final-bridge`
* `integration-before-final`

Use whichever naming pattern best fits the rest of the milestone structure.

---

## Use Note

This prompt is useful when:

* the final version is substantially more complete than the last technical milestone
* later curriculum weeks became more reflective than code-expansive
* the milestone sequence needs an honest technical bridge for instructional comparison
