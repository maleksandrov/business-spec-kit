# /bk.status — Print Current Phase and Artifact State

## Purpose

Give a fast, accurate snapshot of the project: what phase it is in, what has been approved, what is pending, and what the next action is.

---

## Pre-conditions

None. Can be run at any time.

---

## Behavior

**Step 1.** Read all artifacts present:
- `.businesskit/config.md` — project name and type
- `brief.md` — check for unfilled placeholders and open questions
- `strategy.md` — check Status line
- `plan.md` — check Status line
- `execute/` — list all files present and note if any have `Status: Draft` vs `Status: Reviewed`

**Step 2.** Determine current phase:

| Phase | Condition |
|-------|-----------|
| **brief** | `brief.md` exists but `strategy.md` does not, or strategy is not Approved |
| **strategy** | `strategy.md` exists with `Status: Draft` — awaiting approval |
| **plan** | `strategy.md` is Approved but `plan.md` is missing or Draft |
| **execute** | `plan.md` exists and at least one file in `execute/` is present |

**Step 3.** Output a status report in this exact format:

---

```
## business-kit Status — [Project Name]
[Date]

### Current Phase: [brief | strategy | plan | execute]

### Artifacts
| Artifact | Status | Notes |
|----------|--------|-------|
| brief.md | Complete / Incomplete / Missing | [Note any unfilled sections] |
| strategy.md | Approved / Draft / Missing | — |
| plan.md | Complete / Draft / Missing | — |
| execute/[file] | Draft / Reviewed | — |
[list all execute/ files found, or "No execute assets yet"]

### Phase Gate Status
- [x/space] Brief complete         → Unlocks /bk.strategy
- [x/space] Strategy approved      → Unlocks /bk.plan
- [x/space] Plan exists            → Unlocks /bk.execute

### Open Questions
[List any unresolved [ ] items from brief.md or strategy.md, with source file noted]
[Or: "No open questions."]

### Recommended Next Action
[Single specific actionable instruction — e.g. "Review strategy.md and change Status to Approved to unlock /bk.plan"]
```

---

## Rules

- **Report facts, not opinions.** Do not comment on whether the strategy is good — only report structural state.
- **If an artifact is missing, say so clearly.** Do not skip it.
- **The Recommended Next Action must be one specific instruction.** Not a list — the single highest-priority next step.
- **Use `[x]` for completed gates, `[ ]` for pending ones** in the Phase Gate Status section.
