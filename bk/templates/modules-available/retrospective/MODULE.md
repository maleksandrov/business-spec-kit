# Module: retrospective

> AI agent instruction set for the retrospective module.  
> Read this whenever `/bk.retro` is invoked.

## Purpose

Runs a structured retrospective after any project phase or at initiative completion. Captures what was learned, what changed, and what should be encoded into `constitution.md` for future projects.

## Pre-conditions

Before any retrospective command:

1. Read `.businesskit/config.md`
2. Read `.businesskit/constitution.md`
3. Read `.businesskit/glossary.md`

## Commands this module adds

| Command | Description | Output |
|---------|-------------|--------|
| `/bk.retro` | Run a structured retrospective | `execute/retrospective.md` |

## Phase gate rules

`/bk.retro` has no phase gate. It can be run at any point — after a sprint, after a phase, or at project close.

## /bk.retro behavior

Ask exactly **four questions**, strictly one at a time. Never list them. Never ask the next question before receiving an answer to the current one.

**Question 1:**

> "Let's start the retrospective. What did we set out to do — what was the goal or outcome we were working toward?"

Wait for the answer.

**Question 2:**

> "What actually happened? Walk me through it — the key moments, pivots, and how things played out compared to the plan."

Wait for the answer.

**Question 3:**

> "What worked well? I'm looking for things worth repeating — approaches, decisions, habits, or tools that made a positive difference."

Wait for the answer.

**Question 4:**

> "What didn't work? Be specific — what caused friction, delay, or a worse outcome than expected? What would you change?"

After receiving all four answers:

**Step 5.** Ask: "Based on what didn't work, what is the **one specific change** you'd make if you ran this again?"

**Step 6.** Write `execute/retrospective.md` using `retro.template.md`.

**Step 7.** Read `.businesskit/constitution.md` and ask:

> "The retrospective has one lesson worth encoding into your constitution so future projects start smarter. Would you like me to add it? If yes, I'll append it under a 'Lessons Learned' section in constitution.md."

Wait for the user's explicit yes before editing `constitution.md`.

## Rules

- Ask questions strictly one at a time — never list them or batch them
- Do not reframe the user's answers in corporate language — preserve their voice
- "One change for next time" must be a specific, actionable change — not a platitude
- Do not edit `constitution.md` without explicit user consent
- The archive checklist at the bottom of `retro.md` must be filled in based on what actually exists in `.businesskit/`
