# Project-local Codex teaching skills

This archive contains instructions only: no regression implementation, notebook, tests, dependency installer, or global configuration. It was checked against official Codex documentation on 2 November 2026.

## Install in your own project

1. Create or choose your learning project folder and open it in VS Code.
2. Extract this archive into a temporary folder. Inspect its contents.
3. Copy AGENTS.md to your project root. If one already exists, **merge** these tutoring rules into it; do not overwrite existing instructions blindly.
4. Copy the .agents folder to the same project root. Its five skill directories must remain under .agents/skills/.
5. Keep INSTALLATION.md and VALIDATION.md if useful. Nothing goes into your home-level Codex configuration.
6. Open the official Codex extension's sidebar in VS Code and sign in through its normal interface. Work in this project. The extension may present the command “Codex: Open Codex Sidebar”.
7. Ask Codex to list available skills, or use the skill picker (/skills where available). Skills can also be selected with their explicit dollar-prefixed names. If not discovered, check the folder nesting and workspace first, then use a new conversation or the extension's documented refresh/reload workflow.

Expected locations:

- PROJECT/AGENTS.md
- PROJECT/.agents/skills/lr-math-tutor/SKILL.md
- PROJECT/.agents/skills/lr-socratic-mentor/SKILL.md
- PROJECT/.agents/skills/lr-debugging-coach/SKILL.md
- PROJECT/.agents/skills/lr-code-reviewer/SKILL.md
- PROJECT/.agents/skills/lr-learning-evaluator/SKILL.md

Each skill also has optional agents/openai.yaml display metadata. No plugin manifest is needed for this direct project-local skill layout.

## Use one skill at a time

| Need | Prompt to type in Codex |
|---|---|
| Understand an equation | $lr-math-tutor Why does differentiating MSE with respect to w introduce x_i? |
| Implement independently | $lr-socratic-mentor I want to write MSE. Here is my attempt: … Give me one hint, not a solution. |
| Find a bug | $lr-debugging-coach My residual shape is (20,20), but I expected (20,). Here are the input shapes and code: … |
| Review your work | $lr-code-reviewer Review my gradients against full MSE. Do not edit files. Here is my implementation: … |
| Check mastery | $lr-learning-evaluator Test whether I understand one gradient-descent update. Ask one question at a time. |

Implicit selection can also occur when your request matches a skill description. Explicit selection is easier to verify while learning. Provide your attempt, expected output, observed output, and relevant shapes.

If you deliberately want complete code, say so and specify the component: “Show the complete MSE function only, and explain each line.” If you want an actual file edit, request that separately.

## Verify the behavior

Ask the mentor for help with gradient descent without requesting code. It should ask about your attempt, explain a small next step, and not deliver a full training loop. Ask the debugger about (m,) minus (m,1): it should explain broadcasting, suggest a targeted check, and not rewrite the program.

AGENTS.md and skills guide behavior; they are not a security boundary or a guarantee. Higher-priority instructions and more-specific project instructions may affect behavior. An AGENTS.override.md or nested AGENTS.md can change which project rules apply. If the tutor over-solves, explicitly ask it to stop at one hint.

## Maintain the small system

Keep shared boundaries in AGENTS.md and task-specific workflows in the relevant SKILL.md. Edit descriptions when routing is unclear. Recheck one representative prompt after changes. Keep the instructions in your project's Git history. Do not add helper scripts until there is a genuine recurring need.

## Official references

- Skills, discovery, frontmatter, explicit activation: https://developers.openai.com/codex/skills
- Project instructions and precedence: https://developers.openai.com/codex/guides/agents-md
- VS Code integration: https://developers.openai.com/codex/ide

These links may redirect to OpenAI's current documentation host. Repository-scoped .agents/skills, required name/description frontmatter, and optional agents/openai.yaml were verified. Actual discovery in your Windows VS Code session must still be checked there. No global setting has been changed or skill installed by producing this ZIP.
