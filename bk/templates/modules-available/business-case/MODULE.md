# Module: business-case

> AI agent instruction set for the business-case module.  
> Read this whenever `/bk.case`, `/bk.model`, or `/bk.stakeholders` is invoked.

## Purpose

Builds a complete investment justification package: a structured business case document, a three-scenario financial model, and a stakeholder map with communication plan. Used when a decision or funding request requires formal internal approval.

## Pre-conditions

Before any business-case command:

1. Read `.businesskit/config.md`
2. Read `.businesskit/constitution.md`
3. Read `.businesskit/glossary.md`

## Commands this module adds

| Command | Description | Output |
|---------|-------------|--------|
| `/bk.case` | Generate a structured business case document | `execute/business-case.md` |
| `/bk.model` | Generate a three-scenario financial model | `execute/financial-model.md` |
| `/bk.stakeholders` | Generate a stakeholder map and communication plan | `execute/stakeholder-map.md` |

## Phase gate rules

All three commands require `brief.md` to exist with content in the Objective, Constraints, and Success Metrics sections.

## /bk.case — mandatory inputs

**Before generating anything**, ask these four questions in order (one at a time). Do not proceed until all four are answered.

1. "Who is the primary decision-maker for this investment — their name and title?"
2. "What is the decision deadline — the date by which approval is needed?"
3. "What is the budget range being requested — give me a specific number or range?"
4. "Does a financial model already exist, or should I generate one alongside the business case?"

Only after all four are answered, proceed with the business case.

## /bk.case behavior

**Step 1.** Read `brief.md` and extract the problem statement, constraints, and success metrics.

**Step 2.** Collect the four mandatory inputs above.

**Step 3.** Ask two additional questions:

5. "How many options should the business case present? (Three is standard — Option 1: Do Nothing, Option 2: Minimum viable, Option 3: Full investment.)"
6. "What are the top three risks you are aware of today?"

**Step 4.** Write `execute/business-case.md` using `business-case.template.md`.

## /bk.model behavior

**Step 1.** Read `execute/business-case.md` if it exists, otherwise read `brief.md`.

**Step 2.** Ask three questions, one at a time:

1. "What currency and time horizon — e.g. USD, 3 years?"
2. "What discount rate should I use for NPV — if unsure, 10% is a common default."
3. "What are the main cost categories? (e.g. headcount, software licences, infrastructure, professional services)"

**Step 3.** Write `execute/financial-model.md` using `financial-model.template.md` with pessimistic, realistic, and optimistic scenarios.

## /bk.stakeholders behavior

**Step 1.** Read `brief.md` and `execute/business-case.md` if it exists.

**Step 2.** Ask: "Who are the key people who will influence or be affected by this decision — names, titles, and whether they are likely supporters, neutral, or blockers?"

**Step 3.** Write `execute/stakeholder-map.md` using `stakeholder-map.template.md`.

## Rules

- The "Do Nothing" option must always be included in the business case — it is required
- Financial projections must include pessimistic, realistic, and optimistic scenarios
- The executive summary must be exactly 5 sentences
- Every risk must have an owner and a mitigation action
- Never fabricate financial figures — use `[TBC]` if data is not provided
- The ask (final section of business case) must be a single, unambiguous request
