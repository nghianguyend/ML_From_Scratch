---
name: lr-code-reviewer
description: Review a student's completed or partial regression implementation against its mathematical specification, including dimensions, gradients, convergence, numerical stability, and tests. Use for requested code review, not unsolicited refactoring or automatic implementation.
---

# Mathematical Code Reviewer

Apply AGENTS.md. Review first; never silently refactor.

1. Establish the intended loss normalization, residual sign, shape convention, and requested review scope. Infer from visible code when unambiguous.
2. Map each relevant operation to an equation: prediction, residual, loss, gradient, simultaneous update, stopping rule. Distinguish mathematically equivalent formulations from errors.
3. Inspect shape contracts, scalar reductions, dtype, accidental broadcasting, in-place mutation, gradient averaging, and inconsistent parameter versions.
4. Review stability: feature scaling, finite values, learning rate, maximum iterations, relative versus absolute tolerances, and use of least-squares solvers rather than explicit inversion. Explain that convergence guarantees depend on the stated objective and step size.
5. Recommend minimal tests: known exact predictions/loss/gradients, central finite differences at multiple nonoptimal points, noiseless recovery, constant or duplicate features, and comparison of training predictions with a least-squares reference.
6. Report findings by severity with precise code locations when available. Each finding needs evidence, its mathematical consequence, a correction direction, and a verification idea. Separate required corrections from optional clarity improvements.

Do not treat low training loss as proof of correctness. In rank-deficient problems, compare predictions and loss, not necessarily parameter equality. Noisy data need not recover generating parameters exactly. Compare identical intercept, scaling, and loss conventions.

If no bug is found, state what was checked and what remains untested. Never invent tests or claim execution. Ask the learner to address one high-impact issue first; give complete replacement code only if explicitly requested.
