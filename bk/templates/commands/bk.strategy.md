# /bk.strategy — Generate the Strategy

## Purpose

Generate `strategy.md` from `brief.md`. Define the strategic approach, rationale, assumptions, alternatives, risks, and dependencies.

---

## Pre-conditions — CHECK EVERY ONE BEFORE PROCEEDING

### Check 1: brief.md exists

If `brief.md` does not exist:
> "No brief found. Run `/bk.brief` first to define the project intent and context."

Stop. Do not proceed.

### Check 2: All required sections are populated

Check that none of the following sections in `brief.md` are empty or still contain `{{ placeholder }}` text:

- `## Objective`
- `## Context`
- `## Target`
- `## Problem`
- `## Constraints`
- `## Success Metrics`

If any are empty or contain unfilled placeholders:
> "The brief is incomplete. The following sections need to be filled in before strategy can be generated: [list sections]. Run `/bk.clarify` or `/bk.brief --refine` to complete them."

Stop. Do not proceed.

### Check 3: Surface open questions

Read `## Open Questions` in `brief.md`. If there are unresolved items (unchecked `[ ]` boxes):

> "These open questions in the brief could affect the strategy:
> [list them]
> Would you like to resolve them now (recommended), or proceed with what we have?"

If the user chooses to proceed: note which questions remain unresolved in the `## Open Questions` section of `strategy.md`.

### Check 4: Unstated constraints

If any of the following are absent from `brief.md`, ask before proceeding — do not assume:

- **Budget** — is there a budget constraint?
- **Timeline** — is there a hard deadline?
- **Target audience** — is the target specific enough to build strategy from?

---

## Behavior

**Step 1.** Confirm readiness:
> "Brief is complete. Generating strategy based on: [one-sentence summary of the objective]. One moment."

**Step 2.** Read and internalise:
- `brief.md` — all sections
- `.businesskit/constitution.md` — tone, non-negotiables, brand rules
- `.businesskit/glossary.md` — correct terminology

**Step 3.** Generate `strategy.md` with all required sections:

- `## Strategic Approach` — the chosen path in plain language
- `## Rationale` — why this approach over alternatives
- `## Key Assumptions` — what must be true for this to work
- `## Alternatives Considered` — what was rejected and why
- `## Risks` — top 3–5 with likelihood (High/Medium/Low) and mitigation
- `## Dependencies` — external reliances outside your control
- `## Open Questions` — unresolved items that could affect the strategy

**Step 4.** Write `strategy.md` with `Status: Draft` in the header.

**Step 5.** Output:
> "Strategy drafted. Review `strategy.md`. When you're satisfied, change `Status: Draft` to `Status: Approved` — that unlocks `/bk.plan`."

---

## Rules

- **Do NOT assume constraints not stated in the brief.** If something is unclear, ask.
- **Do NOT generate a plan or execution assets in this step.** That is a later phase.
- **Do NOT mark the strategy as Approved.** That is the human's job.
- The strategy must be consistent with every constraint and anti-goal in `brief.md`.
- If the brief contains contradictions (e.g. "close 50 enterprise deals in 2 weeks with one salesperson"), flag them explicitly before generating — do not paper over them.
- The `## Alternatives Considered` section must contain at least two real alternatives, not strawmen.

## Output Format

Write to `strategy.md`. `Status: Draft`. All `{{ placeholder }}` values replaced. HTML comments removed. File is valid Markdown.
