# Module: okr

> AI agent instruction set for the OKR module.  
> Read this whenever `/bk.okr` is invoked.

## Purpose

Converts the success metrics in `brief.md` into structured Objectives and Key Results, links them to the strategy, and appends an OKR section to `strategy.md`. Also produces a standalone `execute/okr.md` for sharing or tracking.

## Pre-conditions

Before any OKR command:

1. Read `.businesskit/config.md`
2. Read `.businesskit/constitution.md`
3. Read `.businesskit/glossary.md`

## Commands this module adds

| Command | Description | Output |
|---------|-------------|--------|
| `/bk.okr` | Convert brief metrics into OKRs | `execute/okr.md` + appended section in `strategy.md` |

## Phase gate rules

`/bk.okr` requires `brief.md` to exist and contain populated content in the **Success Metrics** section.

If `brief.md` does not exist or Success Metrics is empty/unfilled:

> "brief.md must have a completed Success Metrics section before OKRs can be generated. Run `/bk.brief` first."

## /bk.okr behavior

**Step 1.** Read `brief.md` — extract the Success Metrics section and any quantified goals stated elsewhere in the brief.

**Step 2.** Read `strategy.md` if it exists — use it to understand strategic priorities and framing.

**Step 3.** Ask two questions (one at a time):

1. "What time period do these OKRs cover — e.g. Q3 2025, H2 2025, or FY2026?"
2. "Who is the primary owner of these OKRs — a team name, a person's role, or both?"

**Step 4.** Convert each success metric into an OKR:

- The **Objective** must be qualitative, inspirational, and time-bound
- Each **Key Result** must be measurable, specific, and binary or numeric — not a task or activity
- Aim for 1–3 Objectives, each with 2–4 Key Results
- Group related metrics under the same Objective

**Step 5.** Write `execute/okr.md` using `okr.template.md`.

**Step 6.** If `strategy.md` exists, append the OKR summary as a new section at the bottom:

```markdown
## OKRs

_See `execute/okr.md` for full detail._

**Objective 1:** [Objective text]
- KR1: [Key result]
- KR2: [Key result]
```

## Rules

- Key Results must not be activities ("launch X") — they must be outcomes ("increase X by Y%")
- Every KR must have a numeric or binary target that can be graded 0.0–1.0
- The grading guide must explain what 0.7 and 1.0 look like for each KR
- Check-in cadence must be specified (monthly default)
- Do not invent metrics that are not in `brief.md`
