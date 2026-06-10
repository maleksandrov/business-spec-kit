# How business-kit Works

## Overview

business-kit is a CLI that scaffolds a structured folder of markdown files into any project directory. Those files serve as context and commands for your AI assistant (Claude, Copilot, Cursor, Windsurf). The AI reads them automatically when you invoke a slash command.

You stay in control — the AI never advances to the next phase without your explicit approval.

---

## Two-step setup

```
Terminal                          AI assistant
─────────────────────────         ─────────────────────────
bk init --type pitch              Open project folder
  --name "acme-pitch"             Type /bk.brief
  --integration claude            Answer questions
                                  Review brief.md
                                  Type /bk.strategy
                                  ...
```

---

## What `bk init` creates

```
your-project/
├── brief.md                  ← Phase 1 artifact (starts empty)
├── strategy.md               ← Phase 2 artifact
├── plan.md                   ← Phase 3 artifact
├── execute/
│   └── pitch.md              ← Phase 4 artifacts (type-specific)
│   └── deck-outline.md
│   └── objections.md
│
├── .businesskit/
│   ├── config.md             ← Project metadata (name, type, integration)
│   ├── constitution.md       ← Your tone, brand, non-negotiables
│   ├── glossary.md           ← Terms the AI must use correctly
│   └── commands/             ← Internal copies of all slash commands
│
└── .claude/commands/         ← Agent-native command files (if --integration claude)
    ├── bk.brief.md
    ├── bk.strategy.md
    ├── bk.plan.md
    ├── bk.execute.md
    ├── bk.review.md
    ├── bk.status.md
    └── bk.clarify.md
```

For other integrations the agent directory changes:

| Flag | Directory | File suffix |
|------|-----------|-------------|
| `--integration claude` | `.claude/commands/` | `.md` |
| `--integration copilot` | `.github/prompts/` | `.prompt.md` |
| `--integration cursor` | `.cursor/rules/` | `.md` |
| `--integration windsurf` | `.windsurf/rules/` | `.md` |

---

## Phase gate flow

```
 ┌─────────────────────────────────────────────────────────┐
 │  AI assistant session                                   │
 │                                                         │
 │  /bk.brief  ──[you approve]──►  /bk.strategy           │
 │                                    │                    │
 │                              [you approve]              │
 │                                    │                    │
 │                                    ▼                    │
 │                              /bk.plan                  │
 │                                    │                    │
 │                              [you approve]              │
 │                                    │                    │
 │                                    ▼                    │
 │                              /bk.execute               │
 │                                                         │
 │  Anytime:  /bk.clarify   /bk.review   /bk.status       │
 └─────────────────────────────────────────────────────────┘
```

Each command reads the artifact from the previous phase. Nothing is fabricated — the AI always asks you first.

---

## Core commands

| Command | Reads | Writes | Purpose |
|---------|-------|--------|---------|
| `/bk.brief` | `constitution.md`, `glossary.md` | `brief.md` | Guided Q&A to build the business brief |
| `/bk.clarify` | `brief.md` | `brief.md` | Fill gaps or vague sections in the brief |
| `/bk.strategy` | `brief.md` | `strategy.md` | Generate positioning and approach |
| `/bk.plan` | `strategy.md` | `plan.md` | Generate a phased execution plan |
| `/bk.execute` | `plan.md` | `execute/*.md` | Generate all deliverable assets |
| `/bk.review` | all artifacts | — | Audit for gaps and consistency |
| `/bk.status` | all artifacts | — | Show current phase and next action |

---

## Project types

Pass `--type` to pre-populate the right brief template and execution assets.

| Type | Brief focus | Execute assets |
|------|-------------|----------------|
| `pitch` | Investor / customer pitch | pitch.md, deck-outline.md, objections.md |
| `gtm` | Go-to-market launch | gtm.md, email.md, pitch.md |
| `partnership` | Partner or channel deal | partner-brief.md, proposal.md, email.md |
| `strategy` | Internal strategy motion | gtm.md, objections.md |
| `general` | Any other business motion | (blank execute/ — add what you need) |

---

## The `.businesskit/constitution.md` file

This is the most important file to fill in before running any command. It tells the AI:

- Your brand voice and tone
- Things that must always be true (non-negotiables)
- What language / terminology to use
- What to avoid

Every command reads it before writing anything.

---

## Optional modules

Modules extend the framework with domain-specific workflows. See [modules.md](modules.md).

```bash
bk module list          # see what's available
bk module add okr       # install a module
bk module remove okr    # deactivate a module
```
