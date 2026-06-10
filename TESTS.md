# bk CLI — Manual Tests

Run these from a clean temp directory unless noted. Each test shows the command, what to check, and what a pass looks like.

---

## Setup

```bash
# Activate the venv (if not using global install)
source ~/Work/Personal/business-kit/.venv/bin/activate

# Create a scratch directory and enter it
mkdir /tmp/bk-smoke && cd /tmp/bk-smoke
```

---

## T1 — Version

```bash
bk --version
```

**Pass:** prints a version string, e.g. `bk, version 0.1.0`

---

## T2 — Init (defaults)

```bash
mkdir /tmp/bk-t2 && cd /tmp/bk-t2
bk init
```

**Pass:**
- Output says `business-kit initialized`
- Directory name used as project name
- Files created: `.businesskit/config.md`, `.businesskit/constitution.md`, `.businesskit/glossary.md`, `brief.md`, `strategy.md`, `plan.md`
- No `.claude/` or other agent directory created (no `--integration` flag)

---

## T3 — Init with type and name

```bash
mkdir /tmp/bk-t3 && cd /tmp/bk-t3
bk init --type pitch --name "acme-pitch"
```

**Pass:**
- `config.md` contains `project_name: acme-pitch` and `project_type: pitch`
- `execute/` directory exists with pitch-specific files (e.g. `pitch.md`, `deck-outline.md`, `objections.md`)

```bash
cat .businesskit/config.md
ls execute/
```

---

## T4 — All project types

```bash
for TYPE in gtm partnership pitch strategy general; do
  mkdir /tmp/bk-t4-$TYPE && cd /tmp/bk-t4-$TYPE
  bk init --type $TYPE --name "test-$TYPE"
  echo "--- $TYPE execute/ ---"
  ls execute/ 2>/dev/null || echo "(no execute/)"
  cd /tmp
done
```

**Pass:** each type initialises without error; `execute/` contents differ per type.

---

## T5 — Init with Claude integration

```bash
mkdir /tmp/bk-t5 && cd /tmp/bk-t5
bk init --type gtm --name "test-gtm" --integration claude
```

**Pass:**
- `.claude/commands/` directory created
- Contains `bk.brief.md`, `bk.strategy.md`, `bk.plan.md`, `bk.execute.md`, `bk.review.md`, `bk.status.md`, `bk.clarify.md`
- `config.md` shows `integration: claude`

```bash
ls .claude/commands/
grep integration .businesskit/config.md
```

---

## T6 — Init with Copilot integration

```bash
mkdir /tmp/bk-t6 && cd /tmp/bk-t6
bk init --type strategy --integration copilot
```

**Pass:**
- `.github/prompts/` directory created
- Files named `bk.brief.prompt.md`, etc. (`.prompt.md` suffix)

```bash
ls .github/prompts/
```

---

## T7 — Init with Cursor integration

```bash
mkdir /tmp/bk-t7 && cd /tmp/bk-t7
bk init --integration cursor
```

**Pass:** `.cursor/rules/` directory created with `bk.*.md` files.

---

## T8 — Init with Windsurf integration

```bash
mkdir /tmp/bk-t8 && cd /tmp/bk-t8
bk init --integration windsurf
```

**Pass:** `.windsurf/rules/` directory created with `bk.*.md` files.

---

## T9 — Module list (outside a project)

```bash
cd /tmp
bk module list
```

**Pass:** prints available modules with `[ ]` status and descriptions; shows a warning that no `.businesskit/` was found.

---

## T10 — Module list (inside a project)

```bash
mkdir /tmp/bk-t10 && cd /tmp/bk-t10
bk init
bk module list
```

**Pass:** same module list, no warning about missing `.businesskit/`.

---

## T11 — Module add

```bash
mkdir /tmp/bk-t11 && cd /tmp/bk-t11
bk init --integration claude
bk module add okr
```

**Pass:**
- `.businesskit/modules/okr/` created with module files
- `bk module list` shows `[✓]` or `[x]` next to `okr`
- If integration is `claude`, a command file written to `.claude/commands/`

```bash
bk module list
ls .businesskit/modules/okr/
```

---

## T12 — Module remove

```bash
cd /tmp/bk-t11   # reuse T11 directory
bk module remove okr
```

**Pass:**
- `bk module list` shows `okr` as inactive
- Module files deactivated or removed

---

## T13 — Init is idempotent (re-run in existing project)

```bash
mkdir /tmp/bk-t13 && cd /tmp/bk-t13
bk init --type pitch --name "test"
bk init --type pitch --name "test"
```

**Pass:** second run either succeeds cleanly or warns without crashing. Existing files not overwritten.

---

## T14 — Invalid type rejected

```bash
mkdir /tmp/bk-t14 && cd /tmp/bk-t14
bk init --type invalid-type
```

**Pass:** error message from Click listing valid choices; exit code non-zero.

---

## Cleanup

```bash
rm -rf /tmp/bk-t1 /tmp/bk-t2 /tmp/bk-t3 /tmp/bk-t4-* \
       /tmp/bk-t5 /tmp/bk-t6 /tmp/bk-t7 /tmp/bk-t8 \
       /tmp/bk-t9 /tmp/bk-t10 /tmp/bk-t11 /tmp/bk-t12 \
       /tmp/bk-t13 /tmp/bk-t14 /tmp/bk-smoke
```
