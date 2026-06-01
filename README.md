<div align="center">
<img src="media/logo.svg" alt="business-kit" width="96" height="96">

# business-kit

**Turn a business idea into a brief, strategy, and execution assets — in one session with your AI assistant.**

[![Version](https://img.shields.io/badge/version-0.1.0-blue?style=flat-square)](https://github.com/maleksandrov/business-spec-kit/releases)
[![License: MIT](https://img.shields.io/badge/license-MIT-22c55e?style=flat-square)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![AI Agents](https://img.shields.io/badge/agents-Claude%20·%20Copilot%20·%20Cursor%20·%20Windsurf-7c3aed?style=flat-square)](README.md#-ai-agent-integration)

</div>

---

business-kit is a structured workflow for using AI to produce business documents that are actually ready to use. Instead of dumping a vague prompt and hoping, it guides you through *what you want*, *who it's for*, and *what success looks like* — before the AI writes a single word.

Every output is a Markdown file you own. You review and approve each document before the next one begins.

**Good fit for:** founders writing pitch narratives · BD leads drafting partner proposals · strategy teams building annual plans · operators writing investment cases · anyone who's sent an AI-generated document and immediately regretted it

---

## Table of Contents

- [🗂️ What You Produce](#%EF%B8%8F-what-you-produce)
- [⚡ Get Started](#-get-started)
- [🤖 AI Agent Integration](#-ai-agent-integration)
- [⚙️ How It Works](#%EF%B8%8F-how-it-works)
- [🚦 Phase Gates](#-phase-gates)
- [🔧 Command Reference](#-command-reference)
- [📁 Folder Structure](#-folder-structure)
- [🧩 Modules](#-modules)
- [📐 Preset Examples](#-preset-examples)
- [🎯 Design Principles](#-design-principles)
- [🚫 Out of Scope](#-out-of-scope-v1)
- [📄 License](#-license)

---

## 🗂️ What You Produce

One project folder. Four phases. Everything in plain Markdown files you can paste, share, or edit anywhere.

| Phase | File | What's inside |
|-------|------|---------------|
| **1. Brief** | `brief.md` | Situation, audience, objective, constraints, success criteria |
| **2. Strategy** | `strategy.md` | 2–3 strategic options, recommended path, rationale, open risks |
| **3. Plan** | `plan.md` | Sequenced milestones, owners, dependencies, decision points |
| **4. Execute** | `execute/*.md` | Pitch narrative · proposal · email sequence · deck outline · objection map · GTM motion |

Each phase requires your explicit approval before the next one starts. The AI never skips ahead.

> **Example:** A Series A pitch project produces `brief.md` (the story and the ask), `strategy.md` (narrative options and recommended angle), `plan.md` (prep timeline and rehearsal schedule), and `execute/pitch.md` + `execute/deck.md` + `execute/objections.md`.

---

## ⚡ Get Started

### 1. Install

**Recommended — with [`uv`](https://docs.astral.sh/uv/) (no virtualenv needed):**

```bash
uv tool install business-kit --from git+https://github.com/maleksandrov/business-spec-kit.git
```

**Or with pip:**

```bash
pip install git+https://github.com/maleksandrov/business-spec-kit.git
```

**Or from source:**

```bash
git clone https://github.com/maleksandrov/business-spec-kit.git
cd business-spec-kit
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

For native AI agent integration — slash commands written directly into your agent's directory:

```bash
bk init --integration claude    # Claude Code  →  .claude/commands/
bk init --integration copilot   # GitHub Copilot  →  .github/prompts/
bk init --integration cursor    # Cursor  →  .cursor/rules/
bk init --integration windsurf  # Windsurf  →  .windsurf/rules/
```

You can combine flags:

```bash
bk init --type pitch --name "series-a-2026" --integration copilot
```

### 3. Set your constitution

Open `.businesskit/constitution.md` and fill in your tone, brand voice, and non-negotiables. This file is included in every AI invocation. Five minutes here prevents hours of off-brand rewrites.

### 4. Start your brief

In your AI assistant, with the project folder open:

```
/bk.brief
```

The agent guides you through the brief one question at a time. When complete, it writes `brief.md`.

### 5. Generate strategy, plan, and execution assets

```
/bk.strategy             # After brief.md is complete
/bk.plan                 # After strategy.md is approved
/bk.execute pitch        # Or: proposal, email, deck, gtm, partner, objections
```

---

## 🤖 AI Agent Integration

The `--integration` flag wires slash commands directly into your AI agent's native directory so they appear automatically without any manual file loading.

```bash
bk init --integration claude     # Claude Code
bk init --integration copilot    # GitHub Copilot
bk init --integration cursor     # Cursor
bk init --integration windsurf   # Windsurf
```

| Integration | Command files written to | File format |
|-------------|--------------------------|-------------|
| `claude` | `.claude/commands/` | `.md` — available as `/bk.*` slash commands |
| `copilot` | `.github/prompts/` | `.prompt.md` — with `mode: 'agent'` frontmatter |
| `cursor` | `.cursor/rules/` | `.md` — auto-attached as context rules |
| `windsurf` | `.windsurf/rules/` | `.md` — auto-attached as context rules |
| *(none)* | `.businesskit/commands/` | `.md` — load manually when invoking |

`.businesskit/commands/` is **always written** as the universal fallback regardless of integration choice.

The chosen integration is stored in `.businesskit/config.md`. When you later run `bk module add [name]`, the module's instruction file is automatically written to the same agent directory — no extra flags needed.

---

## ⚙️ How It Works

business-kit is entirely file-based and AI-agnostic. The CLI scaffolds a folder with:

- **Markdown templates** — artifact files with structured placeholder syntax
- **Command instruction files** — `.md` files that tell your AI agent exactly what to do for each slash command
- **A constitution** — a persistent context file that keeps outputs on-brand

```
/bk.brief  →  /bk.strategy  →  /bk.plan  →  /bk.execute
```

Your AI agent reads the instruction files. You review and approve each artifact before the next phase unlocks.

---

## 🚦 Phase Gates

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

## 🔧 Command Reference

### CLI commands

| Command | Description |
|---------|-------------|
| `bk init` | Scaffold `.businesskit/` folder and artifact files |
| `bk init --type [gtm\|partnership\|pitch\|strategy]` | Scaffold with a preset |
| `bk init --name [name]` | Set project name (default: directory name) |
| `bk init --integration [claude\|copilot\|cursor\|windsurf]` | Write commands to agent-native directory |
| `bk module list` | List all available modules and their status |
| `bk module add [name]` | Install a module into `.businesskit/modules/` |
| `bk module remove [name]` | Deactivate a module (files are kept) |
| `bk --version` | Show version |

### Slash commands

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

## 📁 Folder Structure

After `bk init`:

```
project-root/
├── .businesskit/
│   ├── config.md          # Project name, type, integration, active modules
│   ├── constitution.md    # Tone, brand voice, non-negotiables — edit this first
│   ├── glossary.md        # Domain terms the AI must use correctly
│   └── commands/          # Universal fallback — one .md per slash command
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
```

With `--integration claude` (same structure for other agents):

```
project-root/
├── .claude/
│   └── commands/          # Native Claude slash commands (mirrors .businesskit/commands/)
│       ├── bk.brief.md
│       ├── bk.strategy.md
│       └── ...
└── .businesskit/          # Universal fallback (always present)
```

After `bk module add [name]`:

```
project-root/
├── .businesskit/
│   └── modules/[name]/
│       ├── MODULE.md      # AI instruction file for this module
│       └── *.template.md  # Artifact templates
└── .claude/commands/
    └── bk.[name].md       # Also written to agent dir automatically
```

---

## 🧩 Modules

Modules extend business-kit with optional frameworks. Install only what you need.

```bash
bk module list          # see what's available
bk module add [name]    # install a module
bk module remove [name] # deactivate (files kept)
```

| Module | What it adds | New commands |
|--------|-------------|-------------|
| `scrum` | Run iterative delivery cycles: turn your plan into sprints, track progress, surface blockers | `/bk.sprint` |
| `itil` | Define service levels, escalation paths, and SLA commitments for ongoing operations | `/bk.sla` |
| `safe` | Scale initiatives across multiple teams: programme increments, value streams, risk tracking | `/bk.pi` |
| `okr` | Convert your strategy metrics into Objectives and Key Results with quarterly check-in templates | `/bk.okr` |
| `rfp-issue` | Write an RFP and score vendor responses with structured evaluation criteria — when you're the buyer | `/bk.rfp`, `/bk.scorecard`, `/bk.vendor-questions` |
| `rfp-respond` | Write a winning proposal response to a client RFP, with a compliance matrix — when you're the vendor | `/bk.rfp-response`, `/bk.compliance-matrix` |
| `business-case` | Build an approval-ready investment justification: exec summary, three options, financial model, stakeholder map | `/bk.case`, `/bk.model`, `/bk.stakeholders` |
| `governance` | Track decisions and compliance obligations throughout the project — nothing falls through the cracks | `/bk.log`, `/bk.compliance` |
| `retrospective` | Run a structured lessons-learned review after any initiative, deal, or launch | `/bk.retro` |

### Worked example: business case approval

Your executive team needs a formal investment justification.

```bash
cd my-project
bk module add business-case
```

Installs `business-case`, `financial-model`, and `stakeholder-map` templates into `.businesskit/modules/business-case/`.

Then in your AI assistant:

```
/bk.brief         # Complete the brief as normal
/bk.case          # Generates execute/business-case.md
/bk.model         # Generates execute/financial-model.md (3-year pessimistic/realistic/optimistic)
/bk.stakeholders  # Generates execute/stakeholder-map.md with approval sequence
```

The `/bk.case` command asks four mandatory questions before generating anything: primary decision-maker, approval deadline, budget range, and whether a financial model already exists. It never skips these.

---

## 📐 Preset Examples

### GTM Launch (`--type gtm`)

```bash
bk init --type gtm --name "acme-launch-q3" --integration copilot
```

Pre-creates: `brief.md` (with ICP, positioning, channels, launch timeline prompts), `execute/gtm.md`, `execute/email.md`, `execute/pitch.md`

```
/bk.brief             # Define ICP, positioning, and channels
/bk.strategy          # Define GTM approach and sequencing logic
/bk.plan              # Sequence launch activities week by week
/bk.execute email     # Outreach sequences for each channel
/bk.execute gtm       # Full launch motion with content plan
```

---

### Partnership (`--type partnership`)

```bash
bk init --type partnership --name "acme-stripe-partnership" --integration claude
```

Pre-creates: `brief.md` (with partner profile, value exchange, integration depth prompts), `execute/partner-brief.md`, `execute/proposal.md`, `execute/email.md`

```
/bk.brief             # Define the partner, value exchange, and goals
/bk.strategy          # Define partnership approach and prioritisation logic
/bk.plan              # Sequence outreach, negotiation, and close
/bk.execute email     # First outreach sequence
/bk.execute partner   # Partnership brief to send to the prospect
```

---

### Pitch (`--type pitch`)

```bash
bk init --type pitch --name "series-a-2026" --integration cursor
```

Pre-creates: `brief.md` (with investor/client type, ask, proof points, objections prompts), `execute/pitch.md`, `execute/deck-outline.md`, `execute/objections.md`

```
/bk.brief                  # Define audience, the ask, and proof points
/bk.strategy               # Define narrative strategy and positioning
/bk.execute pitch          # Full pitch narrative
/bk.execute deck           # Slide-by-slide structure with speaker notes
/bk.execute objections     # Objection map for every anticipated pushback
```

---

### Strategy (`--type strategy`)

```bash
bk init --type strategy --name "2026-annual-strategy"
```

Pre-creates: `brief.md` (with business context, time horizon, decision criteria prompts), `execute/gtm.md`, `execute/objections.md`

```
/bk.brief           # Define the strategic question, context, and constraints
/bk.strategy        # Develop options with rationale and recommendation
/bk.plan            # Sequence strategic initiatives and decision points
/bk.execute gtm     # Go-to-market implications of the chosen strategy
```

---

## 🎯 Design Principles

| Principle | Description |
|-----------|-------------|
| Intent-first | Define the *why* and *what* before any execution begins |
| Human-in-the-loop | You review and approve each document before the next phase starts |
| Works with any AI | Claude, ChatGPT, Copilot, Cursor, Gemini — any assistant that can read files |
| Everything is a file | Every output is a plain `.md` file you own, can edit, and can share |
| Scale-neutral | Useful for a solo founder and a BD team of 50 equally |
| No accounts or subscriptions | No network dependency — runs entirely on your machine |

---

## 🚫 What's intentionally not here

business-kit keeps you in control at every step. Some things are absent by design:

- **No web interface** — your files live on your machine, not in someone else's SaaS account
- **No CRM / Slack / Notion sync** — copy-paste is intentional; the files work everywhere already
- **No multi-user real-time editing** — one owner reviews and approves each phase
- **No auto-run pipelines** — the AI never moves to the next phase without your explicit sign-off

---

## 💬 Support

Open a [GitHub issue](https://github.com/maleksandrov/business-spec-kit/issues/new) for bug reports, feature requests, or questions.

---

## 📄 License

MIT — see [LICENSE](LICENSE) for details.
