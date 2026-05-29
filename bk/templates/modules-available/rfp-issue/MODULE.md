# Module: rfp-issue

> AI agent instruction set for the rfp-issue module.  
> Read this whenever `/bk.rfp`, `/bk.scorecard`, or `/bk.vendor-questions` is invoked.

## Purpose

Enables organizations issuing an RFP (Request for Proposal) to write a complete RFP document, a weighted vendor evaluation scorecard, and a vendor question bank. This module is for the **buyer** side.

> **Note:** If the `rfp-respond` module is also active, warn the user:
> "You have both `rfp-issue` and `rfp-respond` active. These serve opposite roles (buyer vs. vendor). This is unusual — consider whether you meant to activate one or the other."

## Pre-conditions

Before any rfp-issue command:

1. Read `.businesskit/config.md`
2. Read `.businesskit/constitution.md`
3. Read `.businesskit/glossary.md`

## Commands this module adds

| Command | Description | Output |
|---------|-------------|--------|
| `/bk.rfp` | Generate a complete Request for Proposal document | `execute/rfp.md` |
| `/bk.scorecard` | Generate a weighted vendor evaluation scorecard | `execute/scorecard.md` |
| `/bk.vendor-questions` | Generate a bank of due-diligence questions to send vendors | `execute/vendor-questions.md` |

## Phase gate rules

All three commands require `brief.md` to exist.

If `brief.md` does not exist: "Run `/bk.brief` first to establish the project context before generating RFP documents."

## /bk.rfp behavior

**Step 1.** Read `brief.md` and extract: the problem being solved, target audience, known constraints, and success criteria.

**Step 2.** Ask five questions, one at a time:

1. "What is the submission deadline for vendor responses?"
2. "Is there a defined budget range you are willing to share in the RFP, or should it remain undisclosed?"
3. "What are the top 3 functional requirements — things the solution must do?"
4. "Are there any non-negotiable technical requirements (e.g. on-premise deployment, specific API, security certifications)?"
5. "How will you evaluate vendors — what are the most important criteria?"

**Step 3.** Write `execute/rfp.md` using `rfp.template.md`.

## /bk.scorecard behavior

**Step 1.** Read `brief.md` and `execute/rfp.md` if it exists.

**Step 2.** Ask one question: "How many vendors are you evaluating, and what are their names (or use Vendor A, B, C if preferred)?"

**Step 3.** Write `execute/scorecard.md` using `scorecard.template.md` with the evaluation criteria populated from `rfp.md` or `brief.md`.

## /bk.vendor-questions behavior

**Step 1.** Read `execute/rfp.md` — extract all requirements (functional, non-functional, technical).

**Step 2.** Generate a bank of 15–25 due-diligence questions organized by category:
- Company and financial stability
- Technical capability
- Implementation approach
- Support and SLA
- Security and compliance
- Pricing and commercials

**Step 3.** Write `execute/vendor-questions.md` (plain Markdown table, no template required).

## Rules

- The RFP must include both in-scope and out-of-scope items — never omit out-of-scope
- Evaluation criteria in the scorecard must have explicit weightings that sum to 100%
- Scoring guide must be defined (1–5 with descriptions) before the scorecard is populated
- Do not reveal budget range in the RFP unless the user explicitly says to include it
