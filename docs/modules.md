# Modules

Optional modules extend business-kit with domain-specific workflows. Each module adds files to `.businesskit/modules/<name>/` and writes extra slash commands to your agent directory.

Install with:
```bash
bk module add <name>
bk module remove <name>
bk module list
```

---

## okr

**When to use:** You want to convert strategy-level metrics into Objectives and Key Results.

**Adds command:** `/bk.okr`

**What `/bk.okr` does:**
- Reads `brief.md` (success metrics section) and `strategy.md`
- Generates a structured OKR set: Objectives with 2–4 Key Results each
- Ties each KR back to a specific brief metric so nothing is invented

**Good for:** Strategy motions, market entries, product launches, annual planning.

---

## scrum

**When to use:** Your execution plan will be delivered in sprints.

**Adds command:** `/bk.sprint`

**What `/bk.sprint` does:**
- Reads `plan.md`
- Generates a sprint structure: sprint goals, backlog items, definition of done
- Tracks velocity assumptions based on plan constraints

**Good for:** Product teams, engineering projects, any time-boxed delivery.

---

## itil

**When to use:** You're delivering or managing a service and need SLA definitions.

**Adds command:** `/bk.sla`

**What `/bk.sla` does:**
- Reads `brief.md` and `strategy.md`
- Generates a service definition with SLA targets, escalation paths, and value chain checklist

**Good for:** IT service delivery, managed service proposals, internal platform teams.

---

## safe

**When to use:** You're working within a SAFe (Scaled Agile Framework) environment.

**Adds command:** `/bk.pi`

**What `/bk.pi` does:**
- Reads `plan.md`
- Generates a PI (Program Increment) planning structure with value streams, ARTs, and a ROAM risk log

**Good for:** Enterprise engineering organisations running SAFe at scale.

---

## rfp-issue

**When to use:** You are the **buyer** running a formal vendor selection process.

**Adds commands:** `/bk.rfp`, `/bk.scorecard`, `/bk.vendor-questions`

| Command | Output |
|---------|--------|
| `/bk.rfp` | Full RFP document |
| `/bk.scorecard` | Weighted vendor evaluation scorecard |
| `/bk.vendor-questions` | Clarification questions to send vendors |

**Good for:** IT procurement, legal, finance, operations — any team selecting a vendor through a formal process.

> Cannot be installed alongside `rfp-respond` in the same project.

---

## rfp-respond

**When to use:** You are the **vendor** responding to an inbound RFP.

**Adds commands:** `/bk.rfp-response`, `/bk.compliance-matrix`

| Command | Output |
|---------|--------|
| `/bk.rfp-response` | Structured response aligned to the RFP's sections |
| `/bk.compliance-matrix` | Requirement-by-requirement compliance table |

**Good for:** Sales teams, account executives, proposal managers responding to formal procurement.

> Cannot be installed alongside `rfp-issue` in the same project.

---

## business-case

**When to use:** You need to justify a budget, headcount, or investment to a decision-maker.

**Adds commands:** `/bk.case`, `/bk.model`, `/bk.stakeholders`

| Command | Output |
|---------|--------|
| `/bk.case` | Full business case narrative |
| `/bk.model` | Financial model (cost, ROI, payback period) |
| `/bk.stakeholders` | Stakeholder map with interests and concerns |

**Good for:** Internal approvals, board presentations, procurement justifications, headcount requests.

---

## governance

**When to use:** You need to maintain a decision log or run compliance checks on a project.

**Adds commands:** `/bk.log`, `/bk.compliance`

| Command | Output |
|---------|--------|
| `/bk.log` | Decision log with date, owner, rationale, and status |
| `/bk.compliance` | Compliance checklist and audit trail |

**Good for:** Regulated industries, large organisations, any project with formal sign-off requirements.

---

## retrospective

**When to use:** A project or phase has ended and you want to document what happened.

**Adds command:** `/bk.retro`

**What `/bk.retro` does:**
- Reads `brief.md` and any notes you've added to the project folder
- Generates a structured retrospective: what went well, what didn't, themes, action items
- Formats for the retrospective style in your `constitution.md` (Start/Stop/Continue, 4Ls, etc.)

**Good for:** Post-launch reviews, quarterly retrospectives, sprint retrospectives, post-mortems.

---

## Module compatibility

| | okr | scrum | itil | safe | rfp-issue | rfp-respond | business-case | governance | retrospective |
|--|--|--|--|--|--|--|--|--|--|
| **okr** | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| **rfp-issue** | ✓ | ✓ | ✓ | ✓ | — | ✗ | ✓ | ✓ | ✓ |
| **rfp-respond** | ✓ | ✓ | ✓ | ✓ | ✗ | — | ✓ | ✓ | ✓ |

All other modules are compatible with each other. Only `rfp-issue` and `rfp-respond` conflict.
