# /bk.review — Review All Artifacts for Consistency and Gaps

## Purpose

Audit the full set of business-kit artifacts for completeness, internal consistency, and readiness to proceed. Produce a structured report. Do not auto-fix issues — report them and let the human decide.

---

## Pre-conditions

None. `/bk.review` can be run at any phase.

---

## Behavior

**Step 1.** Take inventory. List every artifact present:
- `.businesskit/config.md`
- `.businesskit/constitution.md`
- `.businesskit/glossary.md`
- `brief.md`
- `strategy.md`
- `plan.md`
- Any files in `execute/`

**Step 2.** For each artifact found, check:

| Check | Description |
|-------|-------------|
| **Completeness** | No `{{ placeholder }}` values remain unfilled |
| **Consistency** | Claims do not contradict claims in other artifacts |
| **Status** | Artifact is in the expected state for the current phase |
| **Gaps** | Information missing that will be needed in a later phase |

**Step 3.** Run specific cross-artifact consistency checks:

- Does the objective in `brief.md` match the framing in `strategy.md` and `plan.md`?
- Are the constraints in `brief.md` respected in `plan.md`? (budget, timeline, team size)
- Are the success metrics in `brief.md` reflected as checkpoints or milestones in `plan.md`?
- Does the target audience in `brief.md` match the audience assumed in `execute/` assets?
- Do tone, terminology, and brand language in all artifacts match `.businesskit/constitution.md`?
- Are terms used consistently with `.businesskit/glossary.md`?

**Step 4.** Output a structured report in this exact format:

---

```
## /bk.review Report — [Date]

### Artifacts Found
| Artifact | Present | Status |
|----------|---------|--------|
| brief.md | Yes/No | Complete / Incomplete / Empty |
| strategy.md | Yes/No | Approved / Draft / Empty / Missing |
| plan.md | Yes/No | Complete / Incomplete / Empty / Missing |
| execute/[file] | Yes/No | Draft / Reviewed |
[continue for all files found]

### Issues
[Numbered list. For each issue: artifact name, issue type, specific description, suggested fix]

Example:
1. **brief.md — Incomplete**: Section `## Target` says "enterprise companies" with no industry, company size, or decision-maker title specified. Run `/bk.clarify` to add specifics.

2. **plan.md — Constraint violation**: Timeline in `plan.md` runs 16 weeks but `brief.md` states a 10-week deadline. Flag and revise before execution begins.

### Consistency Warnings
[Any contradictions between artifacts. Be specific — name the exact section and the conflicting claim.]

### Readiness Assessment
- Brief:    [Complete | Incomplete | Missing]
- Strategy: [Approved | Draft | Missing]
- Plan:     [Complete | Draft | Missing]
- Execute:  [list assets present and their status, or "None yet"]

### Recommended Next Action
[Single most important next step — specific and actionable]
```

---

## Rules

- **Be specific.** Do not say "the brief could be stronger" — say exactly which section, what is weak, and what would fix it.
- **Flag contradictions even if minor.** Small contradictions compound in execution.
- **Do not auto-fix.** Report issues and let the human decide what to change.
- **Do not editorialize** about strategic choices — only flag structural problems and inconsistencies.
