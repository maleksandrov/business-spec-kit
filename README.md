# business-kit

> Spec-driven methodology for business development.

business-kit brings the discipline of Spec-Driven Development to business operations. Instead of dumping a vague prompt and hoping, it forces you to define *intent*, *context*, and *success criteria* before an AI generates a single word of strategy, plan, or pitch.

Every phase is gated. Every output is a versioned Markdown file. You review and approve each artifact before the next phase begins.

---

## Quickstart

### 1. Install

```bash
pip install business-kit
```

Or from source:

```bash
git clone https://github.com/your-org/business-kit
cd business-kit
pip install -e .
```

### 2. Initialise a project

Navigate to any project folder and run:

```bash
bk init
```

For a specific business motion:

```bash
bk init --type gtm          # Go-to-market launch
bk init --type partnership  # BD / partnership development
bk init --type pitch        # Investor or client pitch
bk init --type strategy     # Strategic planning
```

You can also name the project:

```bash
bk init --type pitch --name "series-a-2026"
```

### 3. Set your constitution

Open `.businesskit/constitution.md` and fill in:
- Your tone and brand voice
- Non-negotiables (things that must always or never appear in outputs)
- Who you are and who you're not

This file is read on every AI invocation. Five minutes here prevents hours of off-brand rewrites.

### 4. Start your brief

In your AI assistant (Claude, GPT, Gemini), with the project folder open:

```
/bk.brief
```

The agent guides you through the brief one question at a time. When complete, it writes `brief.md`.

### 5. Generate strategy, plan, and execution assets

```
/bk.strategy    # After brief.md is complete
/bk.plan        # After strategy.md is approved
/bk.execute pitch       # Or any of: proposal, email, deck, gtm, partner, objections
```

---

## How It Works

business-kit is entirely file-based and AI-agnostic. The CLI scaffolds a folder with:

- **Markdown templates** — artifact files with structured placeholder syntax
- **Command instruction files** — `.md` files in `.businesskit/commands/` that tell your AI agent exactly what to do for each slash command
- **A constitution** — a persistent context file that keeps outputs on-brand

```
/bk.brief  →  /bk.strategy  →  /bk.plan  →  /bk.execute
```

Your AI agent reads the instruction files. You review and approve each artifact before the next phase unlocks.

---

## Phase Gates

| Phase | Command | Output | Gate to unlock next phase |
|-------|---------|--------|--------------------------|
| 1. Brief | `/bk.brief` | `brief.md` | All sections must be populated |
| 2. Strategy | `/bk.strategy` | `strategy.md` | Change `Status: Draft` → `Status: Approved` |
| 3. Plan | `/bk.plan` | `plan.md` | `plan.md` must exist |
| 4. Execute | `/bk.execute [type]` | `execute/` folder | Review before use |

**Phase gate rules enforced by the AI:**
1. `/bk.strategy` will not run if `brief.md` is incomplete or contains unfilled sections
2. `/bk.plan` will not run unless `strategy.md` has `Status: Approved`
3. `/bk.execute` will not run unless `plan.md` exists
4. The AI surfaces open questions before generating strategy and asks you to resolve them
5. The AI never assumes unstated constraints — if budget, timeline, or audience is missing, it asks

---

## Command Reference

### CLI commands (run in your terminal)

| Command | Description |
|---------|-------------|
| `bk init` | Scaffold `.businesskit/` folder and artifact files |
| `bk init --type [gtm\|partnership\|pitch\|strategy]` | Scaffold with preset templates |
| `bk init --name [name]` | Set project name (default: directory name) |
| `bk module list` | List all available modules and their status |
| `bk module add [name]` | Install a module into `.businesskit/modules/` |
| `bk module remove [name]` | Deactivate a module (files are kept) |
| `bk --version` | Show version |

### Slash commands (run in your AI assistant)

| Command | Description |
|---------|-------------|
| `/bk.brief` | Generate `brief.md` via guided Q&A |
| `/bk.brief --refine` | Improve an existing brief without starting over |
| `/bk.strategy` | Generate `strategy.md` from `brief.md` |
| `/bk.plan` | Generate `plan.md` from the approved `strategy.md` |
| `/bk.execute pitch` | Generate `execute/pitch.md` |
| `/bk.execute proposal` | Generate `execute/proposal.md` |
| `/bk.execute email` | Generate `execute/email.md` |
| `/bk.execute deck` | Generate `execute/deck-outline.md` |
| `/bk.execute gtm` | Generate `execute/gtm.md` |
| `/bk.execute partner` | Generate `execute/partner-brief.md` |
| `/bk.execute objections` | Generate `execute/objections.md` |
| `/bk.review` | Audit all artifacts for consistency and gaps |
| `/bk.status` | Print current phase, approved items, and next action |
| `/bk.clarify` | Guided Q&A to fill gaps in brief, one question at a time |

---

## Folder Structure

After `bk init`:

```
project-root/
├── .businesskit/
│   ├── config.md          # Project name, type, AI agent preference
│   ├── constitution.md    # Tone, brand voice, non-negotiables — edit this first
│   ├── glossary.md        # Domain terms the AI must use correctly
│   └── commands/          # AI instruction files (one per slash command)
│       ├── bk.brief.md
│       ├── bk.strategy.md
│       ├── bk.plan.md
│       ├── bk.execute.md
│       ├── bk.review.md
│       ├── bk.status.md
│       └── bk.clarify.md
├── brief.md               # Phase 1: the business brief
├── strategy.md            # Phase 2: the strategy
├── plan.md                # Phase 3: the execution plan
└── execute/               # Phase 4: execution assets
    ├── pitch.md
    ├── proposal.md
    └── ...
```

After `bk module add [name]`:

```
project-root/
└── .businesskit/
    └── modules/
        └── [name]/           # Module templates and instruction files
            ├── MODULE.md     # AI agent instructions for this module
            └── *.template.md # Artifact templates added by the module
```

---

## Modules

Modules extend business-kit with optional frameworks. Install only what you need.

```bash
bk module list          # see what's available
bk module add [name]    # install a module
bk module remove [name] # deactivate (files kept)
```

| Module | What it adds | New commands |
|--------|-------------|-------------|
| `scrum` | Sprint planning, backlog, velocity tracking | `/bk.sprint` |
| `itil` | Service level definitions and escalation paths | `/bk.sla` |
| `safe` | SAFe PI planning with value streams and ROAM risk log | `/bk.pi` |
| `okr` | Convert brief metrics into Objectives and Key Results | `/bk.okr` |
| `rfp-issue` | Write RFPs and vendor evaluation scorecards (buyer) | `/bk.rfp`, `/bk.scorecard`, `/bk.vendor-questions` |
| `rfp-respond` | Write proposal responses to incoming RFPs (vendor) | `/bk.rfp-response`, `/bk.compliance-matrix` |
| `business-case` | Investment justification with financial model | `/bk.case`, `/bk.model`, `/bk.stakeholders` |
| `governance` | Decision log and compliance checklist | `/bk.log`, `/bk.compliance` |
| `retrospective` | Structured lessons-learned after any initiative | `/bk.retro` |

### Worked example: business case approval

Your executive team needs a formal investment justification.

```bash
cd my-project
bk module add business-case
```

Installs `business-case`, `financial-model`, and `stakeholder-map` templates into `.businesskit/modules/business-case/`.

Then in your AI assistant:

```
/bk.brief
```

The agent guides you through the brief as normal. Once `brief.md` is complete:

```
/bk.case
```

The agent asks four mandatory questions before generating anything:

1. Who is the primary decision-maker?
2. What is the approval deadline?
3. What is the budget range?
4. Does a financial model already exist?

Then it writes `execute/business-case.md` with an executive summary, problem statement, three options (including "Do Nothing"), financial summary, risk log, and a single unambiguous ask.

```
/bk.model
```

Generates `execute/financial-model.md` with pessimistic, realistic, and optimistic 3-year scenarios and a sensitivity analysis.

```
/bk.stakeholders
```

Generates `execute/stakeholder-map.md` with decision-makers, influencers, blockers, and a communication plan with the recommended approval sequence.

---

## Preset Examples

### GTM Launch (`--type gtm`)

For launching a new product, entering a new market, or targeting a new segment.

```bash
bk init --type gtm --name "acme-launch-q3"
```

Pre-creates: `brief.md` (with ICP, positioning, channels, launch timeline prompts), `execute/gtm.md`, `execute/email.md`, `execute/pitch.md`

**Typical workflow:**
1. `/bk.brief` — define ICP, positioning, and channels
2. `/bk.strategy` — define GTM approach and sequencing logic
3. `/bk.plan` — sequence launch activities week by week
4. `/bk.execute email` — outreach sequences for each channel
5. `/bk.execute gtm` — full launch motion with content plan

---

### Partnership (`--type partnership`)

For pursuing a BD relationship, co-sell agreement, or technology integration.

```bash
bk init --type partnership --name "acme-stripe-partnership"
```

Pre-creates: `brief.md` (with partner profile, value exchange, integration depth prompts), `execute/partner-brief.md`, `execute/proposal.md`, `execute/email.md`

**Typical workflow:**
1. `/bk.brief` — define the partner, value exchange, and goals
2. `/bk.strategy` — define partnership approach and prioritisation logic
3. `/bk.plan` — sequence outreach, negotiation, and close
4. `/bk.execute email` — first outreach sequence
5. `/bk.execute partner` — partnership brief to send to the prospect

---

### Pitch (`--type pitch`)

For investor meetings, client pitches, or competitive RFP responses.

```bash
bk init --type pitch --name "series-a-2026"
```

Pre-creates: `brief.md` (with investor/client type, ask, proof points, objections prompts), `execute/pitch.md`, `execute/deck-outline.md`, `execute/objections.md`

**Typical workflow:**
1. `/bk.brief` — define the audience, the ask, and your proof points
2. `/bk.strategy` — define narrative strategy and positioning
3. `/bk.plan` — sequence pitch prep, rehearsal, and follow-up
4. `/bk.execute pitch` — full pitch narrative
5. `/bk.execute deck` — slide-by-slide structure with speaker notes
6. `/bk.execute objections` — objection map for every anticipated pushback

---

### Strategy (`--type strategy`)

For annual planning, competitive response, or major directional decisions.

```bash
bk init --type strategy --name "2026-annual-strategy"
```

Pre-creates: `brief.md` (with business context, time horizon, decision criteria prompts), `execute/gtm.md`, `execute/objections.md`

**Typical workflow:**
1. `/bk.brief` — define the strategic question, context, and constraints
2. `/bk.strategy` — develop options with rationale and recommendation
3. `/bk.plan` — sequence strategic initiatives and decision points
4. `/bk.execute gtm` — go-to-market implications of the chosen strategy

---

## Using with AI Assistants

business-kit works with any AI that can read files in your project directory.

**Claude (claude.ai or Claude desktop app):** Add the project to your context. The slash commands work as natural language instructions that reference the files in `.businesskit/commands/`.

**ChatGPT / Cursor / GitHub Copilot:** Reference or upload the relevant files. The command instruction files work as system prompt additions.

**Gemini and others:** Same approach — include `.businesskit/commands/bk.[command].md` in your context when invoking each slash command.

**Tip:** Always include `.businesskit/constitution.md` in your AI context. It is the single most important file for keeping outputs on-brand. Without it, outputs will be generically correct but brand-wrong.

---

## Design Principles

| Principle | Description |
|-----------|-------------|
| Intent-first | Define the *why* and *what* before any execution begins |
| Phase-gated | Human reviews and approves each artifact before proceeding |
| AI-agnostic | Works with any agent that reads Markdown |
| Artifact-driven | Every output is a versioned `.md` file, not a chat transcript |
| Scale-neutral | Useful for a solo founder and a BD team of 50 equally |
| Offline-first | No network dependency for the core workflow |

---

## Out of Scope (v1)

- Web interface
- SaaS integrations (CRM, Slack, Notion)
- Multi-user collaboration
- Automated AI pipeline execution (human-in-the-loop is intentional)

---

## License

MIT
