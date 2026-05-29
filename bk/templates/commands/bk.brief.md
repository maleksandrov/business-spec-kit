# /bk.brief — Generate or Refine the Business Brief

## Purpose

Generate a complete, structured `brief.md` through guided questions.  
If `brief.md` already exists and is populated, refine it rather than replacing it (unless `--refine` is explicitly invoked).

## Pre-conditions

- Read `.businesskit/config.md` to understand the project type
- Read `.businesskit/constitution.md` for tone, voice, and standing constraints
- Read `.businesskit/glossary.md` for correct terminology

## Phase Gate

This command has no prerequisites — it is the entry point for every project.

If `brief.md` already exists and contains populated content, respond:  
> "A brief already exists. Run `/bk.brief --refine` to improve it without starting over, or tell me explicitly if you want to start from scratch."

---

## Behavior — Starting Fresh

When `brief.md` is empty or does not exist:

**Step 1.** Open the session:
> "I'll guide you through building your business brief one section at a time. This becomes the contract between us — everything the strategy, plan, and execution assets will be built on. Let's start."

**Step 2.** Ask questions for each section **one at a time**, in order:

1. **Objective** — "What does success look like at the end of this? Give me one sentence."
2. **Context** — "Tell me about the company and the situation. What's driving this, and why now?"
3. **Target** — "Who exactly is this for? Be as specific as you can — industry, company size, decision-maker title."
4. **Problem** — "What's the core problem or opportunity you're addressing?"
5. **Constraints** — "What are the hard limits? Budget, timeline, team size, non-negotiables?"
6. **Anti-Goals** — "What is this motion explicitly NOT trying to do?"
7. **Success Metrics** — "How will you know it worked? Give me something measurable."
8. **Open Questions** — "What's still unclesar that could affect the strategy?"

**After each answer:**
- Acknowledge the answer briefly
- Ask one targeted follow-up if the answer is vague or lacks specifics
- Do not move to the next section until the current one is clear enough to build strategy from

**Step 3.** When all sections are complete:
- Write the completed `brief.md` using the project-type template from `.businesskit/config.md`
- Replace every `{{ placeholder }}` with actual content
- Remove all HTML comments
- Output: > "Brief complete. Review `brief.md`, then run `/bk.strategy` when ready."

---

## Behavior — Refinement (`/bk.brief --refine`)

1. Read the existing `brief.md`
2. Identify weak sections: vague language, unfilled placeholders, missing quantification, or thin context
3. Address each weak section with a targeted question — one at a time
4. Rewrite only the sections that are improved — preserve strong sections verbatim
5. Output: > "Brief refined. Review `brief.md`, then run `/bk.strategy` when ready."

---

## Rules

- **Never fabricate content.** If the user hasn't told you something, ask for it.
- **Never skip a required section.** Every section in the brief template is required.
- **If the user says "skip" or "TBD"**, record it as-is and add it to `## Open Questions`.
- **Do not proceed to /bk.strategy from within this command.** That is a separate human-initiated step.
- **Preserve the user's voice.** Do not translate casual answers into corporate language.

## Output Format

Write to `brief.md`. All `{{ placeholder }}` values replaced with actual content. HTML comments removed. File is valid Markdown.
