# /bk.clarify — Structured Clarification Q&A

## Purpose

Work through gaps, ambiguities, and open questions in `brief.md` one question at a time. The output is an updated `brief.md` with every gap filled.

---

## Pre-conditions

`brief.md` must exist.  
If not: > "No brief found. Run `/bk.brief` first to create one."

---

## Behavior

**Step 1.** Read `brief.md` fully.

**Step 2.** Build a prioritised list of gaps. Look for:

| Gap Type | What to Check |
|----------|--------------|
| Unfilled placeholders | Any `{{ placeholder }}` text still present |
| Vague target | "enterprise companies" without size, industry, or decision-maker title |
| Missing quantification | Success metrics without numbers or dates |
| Vague constraints | No budget range, no timeline, no team size |
| Open questions | Unchecked `[ ]` items in `## Open Questions` |
| Thin context | The "why now" or "what's been tried" is missing or one sentence |
| Missing anti-goals | Nothing in `## Anti-Goals` |

**Step 3.** Prioritise gaps by how much they would block strategy generation. Ask the most blocking questions first.

**Step 4.** Ask questions **one at a time**:

- State which section the question is for
- Ask clearly and specifically — not vaguely
- Wait for the answer
- Do NOT dump a list of questions. One at a time, always.

**Step 5.** After each answer:
- Confirm: "Got it. I'll update the [Section name] section."
- Update the relevant section of `brief.md` with the answer in the user's voice
- Ask: "Ready for the next one?"

**Step 6.** If an answer resolves an Open Question, mark it `[x]` in `## Open Questions`.

**Step 7.** If the answer raises a new open question, add it to `## Open Questions`.

**Step 8.** When all gaps are resolved:
> "Brief is complete. All sections are populated and open questions are resolved. Ready to run `/bk.strategy`."

---

## Example Interaction

> **Agent:** "Let's work through your brief. Starting with the most important gap: the **Target** section says 'enterprise customers' — can you be more specific? What industry are they in, and what is the title of the person who makes the buying decision?"

> **User:** "SaaS companies, 200–1000 employees, VP of Sales or CRO."

> **Agent:** "Got it. I'll update the Target section with that. Ready for the next one?"

> **Agent:** "**Success Metrics** currently says 'grow revenue' — can we make that concrete? What number and what timeframe are you targeting?"

> [Continue until brief is complete]

---

## Rules

- **One question at a time.** Never list multiple questions in a single message.
- **Do not make up answers.** If the user doesn't know, record "Unknown — TBD" and move on to the next gap.
- **Do not rephrase answers into corporate language.** Preserve the user's exact voice.
- **Update `brief.md` after each answer** — don't batch updates to the end.
- **Never skip a gap** just because it seems unimportant. Every section is required.
