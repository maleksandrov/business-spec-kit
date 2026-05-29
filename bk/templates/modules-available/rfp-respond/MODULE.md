# Module: rfp-respond

> AI agent instruction set for the rfp-respond module.  
> Read this whenever `/bk.rfp-response` or `/bk.compliance-matrix` is invoked.

## Purpose

Enables organizations responding to an incoming RFP to write a structured proposal response and a compliance matrix that maps each RFP requirement to the proposed solution. This module is for the **vendor** side.

> **Note:** If the `rfp-issue` module is also active, warn the user:
> "You have both `rfp-respond` and `rfp-issue` active. These serve opposite roles (vendor vs. buyer). This is unusual — consider whether you meant to activate one or the other."

## Pre-conditions

Before any rfp-respond command:

1. Read `.businesskit/config.md`
2. Read `.businesskit/constitution.md`
3. Read `.businesskit/glossary.md`

## Commands this module adds

| Command | Description | Output |
|---------|-------------|--------|
| `/bk.rfp-response` | Generate a structured proposal response to an RFP | `execute/rfp-response.md` |
| `/bk.compliance-matrix` | Generate a requirement-by-requirement compliance matrix | `execute/compliance-matrix.md` |

## Phase gate rules

Both commands require `brief.md` to exist.

`/bk.brief` runs in **rfp-respond mode** when this module is active — see below.

## /bk.brief — rfp-respond mode

When this module is active and `/bk.brief` is run, the brief session must extract:

1. **Client requirements** — what the RFP is asking for (full list)
2. **Evaluation criteria** — how the client will score responses
3. **Mandatory sections** — any sections the RFP explicitly requires in the response
4. **Disqualifying conditions** — any requirements that would immediately disqualify a response
5. **Submission deadline** — the exact date and time

Ask for each of these explicitly if they are not in the RFP text provided. Do not proceed with the brief until all five are confirmed.

## /bk.rfp-response behavior

**Step 1.** Read `brief.md` — extract the client's requirements, evaluation criteria, and any constraints.

**Step 2.** Ask four questions, one at a time:

1. "What is the name of your company / the responding organization?"
2. "What is your proposed pricing model — fixed price, time and materials, or subscription? Give me a summary."
3. "Who are the two or three key people on your proposed team, and what are their roles?"
4. "What is your single strongest differentiator for this engagement — the one reason you should win?"

**Step 3.** Write `execute/rfp-response.md` using `rfp-response.template.md`.

## /bk.compliance-matrix behavior

**Step 1.** Read `brief.md` for the full list of client requirements.

**Step 2.** Read `execute/rfp-response.md` if it exists.

**Step 3.** For each stated requirement, map:
- The requirement (verbatim from RFP or brief)
- Compliance status: **Fully Met** / **Partially Met** / **Not Met** / **Not Applicable**
- Where in the response it is addressed (section reference)
- Any caveats or conditions

**Step 4.** Write `execute/compliance-matrix.md` as a Markdown table (no separate template needed).

## Rules

- Never fabricate capabilities — if the user has not told you, ask
- The executive summary must reference the client's evaluation criteria directly
- "Why us" section must be concrete — no generic claims
- Every mandatory RFP section must be addressed in the response
- Compliance matrix must cover 100% of stated requirements
