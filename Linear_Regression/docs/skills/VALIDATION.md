# Validation record

Prepared and checked on 2 November 2026.

## Format and documentation

- Five skill directories, each with a SKILL.md beginning with valid YAML frontmatter containing name and description.
- Names match their lowercase, hyphenated folder names.
- The skill-creator's quick_validate.py accepted all five skills.
- Optional agents/openai.yaml files provide quoted display names, short descriptions, and default prompts that explicitly name the corresponding $skill.
- No placeholder instructions, executable helpers, learner algorithm files, or global configuration are included.
- Project-local discovery under .agents/skills, project AGENTS.md instructions, and explicit skill activation were checked against the official Codex documentation linked in INSTALLATION.md.

## Behavioral checks

Each check used a fresh agent context with the project instructions, one skill, and a concrete learner request. These are smoke checks, not a guarantee of every future response.

| Skill | Learner request | Observed behavior |
|---|---|---|
| Mathematical Tutor | Why does the slope derivative include x_i but the bias derivative does not? | Derived both chain-rule paths, gave a small example, connected to array operations, and ended with an unanswered transfer question. |
| Socratic Coding Mentor | Help start gradient descent; no attempt supplied. | Asked about the attempt, proposed the prediction contract first, and supplied no complete algorithm. |
| Debugging Coach | Predictions (3,) minus targets (3,1) runs but gives wrong loss. | Explained the unintended (3,3) cross-example comparison and proposed a shape check plus an independent known-value test. No rewrite. |
| Mathematical Code Reviewer | Full-MSE code with gradients missing factor 2. | Identified the normalization mismatch, explained its consequence, and suggested finite differences. No edits or claimed execution. |
| Learning Evaluator | One short challenge about a single update. | Set one numerical task with conventions and success evidence; withheld the answer. |

No tests required modifying a learner project, installing packages, or changing settings. The generated ZIP has not been installed in your VS Code environment. Actual skill discovery and instruction precedence must be confirmed in your workspace using INSTALLATION.md.

## Maintenance check after you edit a skill

Confirm valid YAML, meaningful activation criteria, consistent shape/loss conventions, and no accidental full-code default. Repeat the representative prompt above. If an agent gives away too much, tighten the shared boundaries or the specific workflow. Keep only the five focused workflows unless a new recurring need is clearly different.
