# Module: scrum

> AI agent instruction set for the scrum module.  
> Read this whenever `/bk.sprint` is invoked.

## Purpose

Transforms the task list in `plan.md` into sprint-structured delivery cycles: user stories, acceptance criteria, story points, definition of done, and velocity tracking.

## Pre-conditions

Before any scrum command:

1. Read `.businesskit/config.md`
2. Read `.businesskit/constitution.md`
3. Read `.businesskit/glossary.md`

## Commands this module adds

| Command | Description | Output |
|---------|-------------|--------|
| `/bk.sprint` | Break `plan.md` into sprint cycles | `execute/sprint-plan.md` |

## Phase gate rules

`/bk.sprint` requires `plan.md` to exist AND contain `Status: Approved`.

If `plan.md` does not have `Status: Approved`, stop and say:

> "plan.md must be approved before sprint planning can begin. Change `Status: Draft` to `Status: Approved` in plan.md, then re-run `/bk.sprint`."

## /bk.sprint behavior

**Step 1.** Read `plan.md` and extract: all tasks, task dependencies, phases, and timeline constraints.

**Step 2.** Ask about sprint length — one question:

> "What is your preferred sprint length — 1, 2, or 3 weeks?"

Wait for the answer before continuing. Do not proceed with a default.

**Step 3.** Group tasks into sprints:

- Respect dependencies from `plan.md` — a task that depends on another must be in a later sprint
- Keep committed points per sprint realistic — default capacity is 20 points unless the user specifies otherwise
- Keep logically related tasks together when possible
- Do not mix tasks that explicitly belong to different phases unless the user asks

**Step 4.** Convert each plan task into user story format:

> "As a [role], I want [action] so that [outcome]."

If the role or outcome is not derivable from `plan.md`, ask — do not guess.

**Step 5.** Assign story point estimates using Fibonacci: 1, 2, 3, 5, 8.

**Step 6.** Write `execute/sprint-plan.md` using `sprint-plan.template.md`.

## Rules

- Do not reinterpret or rewrite plan tasks — translate them directly into sprint format
- Each sprint must have a one-sentence sprint goal
- The definition of done must contain at least 3 items
- Story point totals per sprint must be stated explicitly
- Never mark a story as committed if it has an unresolved dependency
- Never leave a `{{ placeholder }}` unfilled in the output
