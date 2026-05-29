# Module: governance

> AI agent instruction set for the governance module.  
> Read this whenever `/bk.log` or `/bk.compliance` is invoked.

## Purpose

Maintains a persistent decision log and a compliance checklist throughout the project lifecycle. When this module is active, the agent must prompt to log every significant decision made at a phase gate.

## Pre-conditions

Before any governance command:

1. Read `.businesskit/config.md`
2. Read `.businesskit/constitution.md`
3. Read `.businesskit/glossary.md`

## Commands this module adds

| Command | Description | Output |
|---------|-------------|--------|
| `/bk.log` | Record a decision in the decision log | Appends a row to `decision-log.md` |
| `/bk.compliance` | Run the compliance checklist | `execute/compliance-checklist.md` |

## Phase gate behavior (always active when module is installed)

At every phase gate — whenever the user approves `brief.md`, `strategy.md`, or `plan.md` — the agent must say:

> "Governance is active. Would you like to log this decision? Run `/bk.log` to record it."

This reminder must appear whenever the user signals approval (e.g., changes Status to Approved, says "approve", "looks good", "move forward").

## /bk.log behavior

**Step 1.** Ask three questions in sequence:

1. "What was the decision?"
2. "What is the rationale — why was this the right choice?"
3. "Who made this decision, and what alternatives were considered and rejected?"

**Step 2.** Append a new row to `.businesskit/modules/governance/decision-log.md`:

```
| [auto-incremented #] | [today's date] | [decision] | [rationale] | [made by] | [alternatives rejected] |
```

If `decision-log.md` does not exist yet, create it with the header row first (using `decision-log.template.md`), then append.

**Step 3.** Confirm: "Decision logged. Run `/bk.log` again to log another."

## /bk.compliance behavior

**Step 1.** Read `config.md` — check the `compliance_standards` field.

**Step 2.** Ask: "Which compliance standard should I run the checklist for — GDPR, SOC 2, ISO 27001, HIPAA, or internal governance only?"

**Step 3.** For the selected standard, review the project artifacts in `.businesskit/` and assess each checklist item as:
- **Yes** — evidence found in project artifacts
- **No** — not addressed
- **Partial** — partially addressed, action needed
- **N/A** — not applicable to this project

**Step 4.** Write `execute/compliance-checklist.md` using `compliance-checklist.template.md`.

## Rules

- The decision log must never be edited or deleted by the agent — only appended to
- Every compliance checklist item must have a status — never leave a row blank
- Do not assume compliance — only mark "Yes" if there is explicit evidence in the artifacts
- The sign-off table in compliance-checklist.md must be populated with the names from `brief.md` where available
