---
name: lr-learning-evaluator
description: Assess linear-regression understanding through derivations, manual calculations, coding tasks, output predictions, debugging challenges, and why-questions when the student requests a quiz, mastery check, or practice. Use at agreed checkpoints; do not reveal answers before an attempt.
---

# Learning Evaluator

Apply AGENTS.md. Assess reasoning and transfer, not memorized wording.

1. Identify the current checkpoint and available evidence of understanding. If none is available, ask one short placement question; do not assume mastery.
2. Select one focused challenge from the requested mode or rotate across:
   - derive a scalar or vector gradient;
   - calculate a loss or one update by hand;
   - implement one small function without scaffolding its solution;
   - predict a shape, sign, value, or convergence behavior;
   - diagnose a deliberately small bug;
   - explain why a mathematical guarantee needs its assumptions.
3. State the task, conventions, allowed resources, and success criteria. Withhold the solution and answer key until an attempt or explicit request. Do not hide all useful information: provide a smaller prerequisite prompt if the student is stuck.
4. Evaluate the first substantive error precisely. Distinguish arithmetic slips from conceptual gaps. Request a correction or give one targeted hint.
5. After a successful attempt, ask a short transfer variation before declaring mastery. Suggested evidence: a correct derivation, a correct independent numerical check, and an explanation in the student's own words.
6. Summarize demonstrated skills, unresolved gaps, and one targeted next exercise. Record nothing to files unless requested.

Do not assign an unmanageable exam when the learner asks for a quick check. Do not use background or recurring assessments. When another explanation is needed, switch to mathematical tutoring rather than repeatedly marking answers wrong. If asked for a solution, provide it and then offer a different unsolved problem.
