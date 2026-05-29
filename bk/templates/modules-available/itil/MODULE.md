# Module: itil

> AI agent instruction set for the ITIL module.  
> Read this whenever `/bk.sla` is invoked.

## Purpose

Adds ITIL-aligned service level definitions to any project that involves delivering an ongoing service (as opposed to a one-time initiative). Produces a structured SLA document with priority tiers, response/resolution targets, exclusions, and escalation paths.

## Pre-conditions

Before any ITIL command:

1. Read `.businesskit/config.md`
2. Read `.businesskit/constitution.md`
3. Read `.businesskit/glossary.md`

## Commands this module adds

| Command | Description | Output |
|---------|-------------|--------|
| `/bk.sla` | Generate a service level agreement definition | `execute/sla.md` |

## Phase gate rules

`/bk.sla` has no phase gate — it can run at any time. However, it produces a more accurate output if `brief.md` exists.

If `brief.md` exists, read it first to extract the service being delivered, the target audience, and any existing SLA commitments mentioned.

## /bk.sla behavior

**Step 1.** Check if `brief.md` exists. If it does, read it and extract:
- The service being delivered
- Who the service is delivered to (the customer)
- Any SLA commitments or targets already mentioned

Acknowledge what you found: "Based on your brief, this SLA covers [service] delivered to [customer]. Let me ask a few questions to complete it."

**Step 2.** Ask three questions, one at a time:

1. "What are the operating hours for this service — for example Mon–Fri 09:00–18:00, or 24/7?"
2. "What do P1, P2, and P3 mean in your context? Give me a one-sentence definition for each severity level."
3. "Are there any conditions explicitly excluded from this SLA?"

Wait for each answer before asking the next question.

**Step 3.** Write `execute/sla.md` using `sla.template.md`.

## Rules

- Response and resolution targets must be stated explicitly — do not leave them as `[e.g. 4h]`
- The escalation path must name a specific role, not "the team"
- The review cadence must be specified (quarterly is the default if not stated)
- Never fabricate SLA targets — always ask if not told
