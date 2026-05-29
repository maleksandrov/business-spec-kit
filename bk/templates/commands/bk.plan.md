# /bk.plan — Generate the Execution Plan

## Purpose

Generate `plan.md` from `brief.md` and `strategy.md`. Break the approved strategy into concrete, sequenced, assignable actions with a timeline and defined checkpoints.

---

## Pre-conditions — CHECK EVERY ONE BEFORE PROCEEDING

### Check 1: brief.md exists and is complete

If `brief.md` does not exist or contains unfilled `{{ placeholder }}` values in required sections:
> "Brief not found or incomplete. Run `/bk.brief` and `/bk.strategy` first."

Stop.

### Check 2: strategy.md exists

If `strategy.md` does not exist:
> "No strategy found. Run `/bk.strategy` first."

Stop.

### Check 3: strategy.md is Approved — NON-NEGOTIABLE

Read the header of `strategy.md`. If the status line is anything other than `Status: Approved`:
> "The strategy has not been approved yet. Open `strategy.md`, review it, and change the status line from `Status: Draft` to `Status: Approved`. Then run `/bk.plan` again."

**This check is non-negotiable. Do not proceed without a confirmed `Status: Approved` line.**

---

## Behavior

**Step 1.** Confirm readiness:
> "Strategy is approved. Generating execution plan."

**Step 2.** Read and internalise:
- `brief.md` — objective, constraints, success metrics, timeline hints
- `strategy.md` — strategic approach, key phases implied by the strategy, risks, dependencies
- `.businesskit/constitution.md` — tone, standing constraints

**Step 3.** Derive phases from the strategy. Phases should reflect the strategic logic, not generic project stages. Typical count: 3–5 phases.

**Step 4.** Generate `plan.md` with all required sections:

- `## Phases` — named phases with objectives, derived from the strategy
- `## Tasks` — specific tasks per phase in the mandatory format (see below)
- `## Timeline` — week-by-week or milestone schedule aligned to brief constraints
- `## Resources Required` — people, budget, tools, data inputs
- `## Checkpoints` — defined review gates between phases with go/no-go criteria
- `## Decision Log` — empty table, to be populated during execution

**Mandatory task format:**
```
- [ ] **[TASK-XX]** Task description
  _Owner: [Role] | Effort: [Xh or Xd] | Depends on: [TASK-XX or none] | Phase: [Phase Name]_
```

**Step 5.** Write `plan.md` with `Status: Draft`.

**Step 6.** Output:
> "Plan drafted. Review `plan.md`. When ready to generate execution assets, run `/bk.execute [type]`."

---

## Rules

- **Every task must have**: an owner role, an effort estimate, a dependency reference, and a phase assignment.
- **Tasks must be realistically sequenced.** Dependencies must reflect logical order.
- **The timeline must fit within the constraints in `brief.md`.** If it doesn't, flag the gap explicitly rather than silently overrunning it.
- **Do not skip the Checkpoints section.** Review gates are non-optional.
- **If the strategy implies resources not available per the brief** (e.g. strategy requires 3 engineers but brief says "solo founder"), flag the conflict explicitly.
- Use owner **role titles**, not personal names — plans should survive personnel changes.

## Output Format

Write to `plan.md`. `Status: Draft`. All `{{ placeholder }}` values replaced. HTML comments removed. File is valid Markdown.
