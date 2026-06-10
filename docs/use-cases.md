# Use Cases

Worked examples showing how different roles use business-kit in practice.

---

## Use case 1 — Founder preparing a Series A pitch

**Who:** Solo founder, first institutional fundraise  
**Type:** `pitch`  
**Integration:** `claude`

### Setup

```bash
mkdir acme-series-a && cd acme-series-a
bk init --type pitch --name "acme-series-a" --integration claude
```

### Workflow

1. Open `acme-series-a` as a project in Claude Desktop
2. Edit `.businesskit/constitution.md`:
   - Tone: direct, confident, no fluff
   - Non-negotiable: always lead with the problem, not the solution
3. Run `/bk.brief` — Claude asks about objective, target investor, traction, ask size
4. Review `brief.md`, run `/bk.clarify` if any section is thin
5. Run `/bk.strategy` — Claude writes positioning and narrative arc
6. Run `/bk.plan` — Claude structures the phases (deck → dry runs → outreach)
7. Run `/bk.execute` — produces `pitch.md`, `deck-outline.md`, `objections.md`

### What you end up with

- A structured narrative for the deck
- Slide-by-slide outline
- Pre-answered objection list for due diligence calls

---

## Use case 2 — BD lead running a partnership motion

**Who:** Business development lead at a SaaS company  
**Type:** `partnership`  
**Integration:** `cursor`

### Setup

```bash
mkdir stripe-partnership && cd stripe-partnership
bk init --type partnership --name "stripe-partnership" --integration cursor
```

### Workflow

1. Open in Cursor with the project folder active
2. Fill `.businesskit/constitution.md` with company positioning and deal constraints
3. Run `/bk.brief` — covers partner profile, mutual value, integration scope, success metrics
4. Run `/bk.strategy` — surfaces the narrative for why this partnership works for both sides
5. Run `/bk.execute` — produces `partner-brief.md`, `proposal.md`, `email.md`

### What you end up with

- An internal partner brief for stakeholder sign-off
- A proposal document to share with the partner
- A cold outreach email to initiate the conversation

---

## Use case 3 — Strategy team running a market entry

**Who:** Head of Strategy, entering a new geography  
**Type:** `strategy`  
**Integration:** `copilot`

### Setup

```bash
mkdir apac-entry && cd apac-entry
bk init --type strategy --name "apac-entry" --integration copilot
bk module add okr
```

### Workflow

1. Open in VS Code (GitHub Copilot Chat picks up `.github/prompts/`)
2. Fill constitution with regional constraints and sign-off requirements
3. Run `/bk.brief` — define the market opportunity, ICP, competitive landscape
4. Run `/bk.strategy` — generates positioning and phased entry approach
5. Run `/bk.okr` — converts strategy metrics into Objectives and Key Results
6. Run `/bk.plan` — produces a phased execution roadmap
7. Run `/bk.execute` — generates `gtm.md` and `objections.md`

### What you end up with

- A complete market entry strategy doc
- OKRs tied directly to the brief's success metrics
- A GTM plan and objection-handling guide

---

## Use case 4 — Procurement team issuing an RFP

**Who:** IT Procurement, selecting a new data platform  
**Type:** `general`  
**Integration:** `claude`

### Setup

```bash
mkdir data-platform-rfp && cd data-platform-rfp
bk init --type general --name "data-platform-rfp" --integration claude
bk module add rfp-issue
```

### Workflow

1. Open in Claude Desktop
2. Fill constitution with evaluation criteria and vendor constraints
3. Run `/bk.brief` — define requirements, scope, and evaluation timeline
4. Run `/bk.strategy` — frame the vendor landscape and selection approach
5. Run `/bk.rfp` — generates a full RFP document
6. Run `/bk.scorecard` — generates a weighted vendor evaluation scorecard
7. Run `/bk.vendor-questions` — generates clarification questions to send vendors

### What you end up with

- A publish-ready RFP document
- A vendor scoring matrix
- A structured questions list to send during the vendor Q&A window

---

## Use case 5 — Vendor responding to an RFP

**Who:** Account Executive, responding to an inbound RFP  
**Type:** `general`  
**Integration:** `claude`

### Setup

```bash
mkdir acme-rfp-response && cd acme-rfp-response
bk init --type general --name "acme-rfp-response" --integration claude
bk module add rfp-respond
```

### Workflow

1. Paste or attach the buyer's RFP into the project folder as `rfp-received.md`
2. Fill constitution with your company's strengths and messaging guardrails
3. Run `/bk.brief` — frame your response strategy (what to lead with, what to address)
4. Run `/bk.rfp-response` — generates a structured response aligned to the RFP sections
5. Run `/bk.compliance-matrix` — generates a requirement-by-requirement compliance table

### What you end up with

- A complete, structured RFP response
- A compliance matrix (required for most formal procurement processes)

---

## Use case 6 — Operator building a business case for budget approval

**Who:** Engineering Director, requesting headcount or tooling budget  
**Type:** `general`  
**Integration:** `windsurf`

### Setup

```bash
mkdir eng-headcount-case && cd eng-headcount-case
bk init --type general --name "eng-headcount-case" --integration windsurf
bk module add business-case
```

### Workflow

1. Open in Windsurf
2. Fill constitution with internal language, the approver audience, and financial constraints
3. Run `/bk.brief` — define the problem, investment ask, and expected outcomes
4. Run `/bk.case` — generates the full business case narrative
5. Run `/bk.model` — generates a financial model (cost, ROI, payback period)
6. Run `/bk.stakeholders` — maps stakeholders and their interests/concerns

### What you end up with

- A board-ready business case document
- A financial model to attach
- A stakeholder map to guide the approval conversation

---

## Use case 7 — Team running a post-project retrospective

**Who:** Project Manager, after a product launch  
**Type:** `general`  
**Integration:** `claude`

### Setup

```bash
mkdir q2-launch-retro && cd q2-launch-retro
bk init --type general --name "q2-launch-retro" --integration claude
bk module add retrospective
```

### Workflow

1. Collect notes from the team into a `notes.md` in the project folder
2. Fill constitution with the retrospective format (e.g. Start/Stop/Continue)
3. Run `/bk.brief` — summarise what the project was and what was attempted
4. Run `/bk.retro` — generates a structured retrospective with themes, actions, and owners

### What you end up with

- A clean retrospective document
- Categorised findings and action items
- A shareable summary for the wider team

---

## Combining modules

Modules can be stacked. A strategy motion that also needs OKRs and governance:

```bash
bk init --type strategy --name "fy27-plan" --integration claude
bk module add okr
bk module add governance
```

This gives you `/bk.strategy`, `/bk.okr`, `/bk.log`, and `/bk.compliance` — all reading from the same brief and strategy artifacts.

> Note: `rfp-issue` and `rfp-respond` conflict — you can only install one per project (you're either the buyer or the vendor).
