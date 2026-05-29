# Module: safe

> AI agent instruction set for the SAFe (Scaled Agile Framework) module.  
> Read this whenever `/bk.pi` is invoked.

## Purpose

Reshapes the task list in `plan.md` into a SAFe Program Increment (PI) structure with team objectives, features, ROAM risks, milestones, and cross-team dependencies.

## Pre-conditions

Before any SAFe command:

1. Read `.businesskit/config.md`
2. Read `.businesskit/constitution.md`
3. Read `.businesskit/glossary.md`

## Commands this module adds

| Command | Description | Output |
|---------|-------------|--------|
| `/bk.pi` | Generate a PI Planning output document | `execute/pi-plan.md` |

## Phase gate rules

`/bk.pi` requires `plan.md` to exist AND contain `Status: Approved`.

If `plan.md` does not have `Status: Approved`, stop and say:

> "plan.md must be approved before PI planning. Change `Status: Draft` to `Status: Approved` in plan.md, then re-run `/bk.pi`."

## /bk.pi behavior

**Step 1.** Read `plan.md` and extract: all tasks, phases, timeline, dependencies, and resources.

**Step 2.** Ask four questions in sequence (one at a time):

1. "What is the PI duration — typically 10 weeks. Is that right, or do you use a different cadence?"
2. "What is the PI Objective — the one thing this PI must achieve to be successful?"
3. "How many Agile Release Trains (ARTs) are involved, and what are their names?"
4. "Are there any known dependencies on teams or systems outside this PI?"

Wait for each answer before asking the next.

**Step 3.** Map plan.md tasks to SAFe features and stories. Group by ART and sprint (iteration).

**Step 4.** Identify risks from plan.md and classify each using ROAM:
- **R**esolved — risk eliminated
- **O**wned — someone is accountable for managing it
- **A**ccepted — team acknowledges and proceeds
- **M**itigated — action taken to reduce likelihood or impact

**Step 5.** Write `execute/pi-plan.md` using `pi-plan.template.md`.

## Rules

- Each ART must have at least one team objective
- ROAM classification must be explicit for every identified risk
- Milestones must include a date or sprint reference (not just "TBD")
- Cross-team dependencies must name the dependent team
- Never leave a `{{ placeholder }}` unfilled
