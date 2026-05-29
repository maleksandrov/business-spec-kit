"""business-kit CLI — scaffolds .businesskit/ folder and artifact files."""

from __future__ import annotations

import re
import shutil
from datetime import date
from pathlib import Path

import click

TEMPLATES_DIR = Path(__file__).parent / "templates"

# Which execute/ assets to pre-create for each preset type
PRESET_EXECUTE_ASSETS: dict[str, list[str]] = {
    "gtm":         ["gtm", "email", "pitch"],
    "partnership": ["partner-brief", "proposal", "email"],
    "pitch":       ["pitch", "deck-outline", "objections"],
    "strategy":    ["gtm", "objections"],
    "general":     [],
}

AVAILABLE_MODULES: list[str] = [
    "itil", "scrum", "safe", "okr",
    "rfp-issue", "rfp-respond",
    "business-case", "governance", "retrospective",
]

MODULES_DIR = TEMPLATES_DIR / "modules-available"

# Pairs of modules that serve opposite roles — warn when both are installed
CONFLICTING_PAIRS: list[tuple[str, str]] = [
    ("rfp-issue", "rfp-respond"),
]

MODULE_COMMANDS: dict[str, list[str]] = {
    "scrum":         ["/bk.sprint"],
    "itil":          ["/bk.sla"],
    "safe":          ["/bk.pi"],
    "okr":           ["/bk.okr"],
    "rfp-issue":     ["/bk.rfp", "/bk.scorecard", "/bk.vendor-questions"],
    "rfp-respond":   ["/bk.rfp-response", "/bk.compliance-matrix"],
    "business-case": ["/bk.case", "/bk.model", "/bk.stakeholders"],
    "governance":    ["/bk.log", "/bk.compliance"],
    "retrospective": ["/bk.retro"],
}

MODULE_DESCRIPTIONS: dict[str, str] = {
    "scrum":         "Sprint-structured plans, backlog, velocity tracking",
    "itil":          "Service level definitions and value chain checklist",
    "safe":          "PI planning with value streams, ARTs, and ROAM risk log",
    "okr":           "Convert brief metrics into Objectives and Key Results",
    "rfp-issue":     "Write RFPs and vendor evaluation scorecards (buyer side)",
    "rfp-respond":   "Write proposal responses to incoming RFPs (vendor side)",
    "business-case": "Investment justification with financial model and stakeholder map",
    "governance":    "Decision log, compliance checklist, and audit trail",
    "retrospective": "Structured lessons-learned after any initiative",
}


def _write_if_new(path: Path, content: str) -> bool:
    """Write content to path only if the file does not already exist. Returns True if written."""
    if path.exists():
        return False
    path.write_text(content, encoding="utf-8")
    return True


def _render_config(project_type: str, project_name: str) -> str:
    template = (TEMPLATES_DIR / "config.md").read_text(encoding="utf-8")
    return (
        template
        .replace("{{ project_name }}", project_name)
        .replace("{{ project_type }}", project_type)
        .replace("{{ created }}", date.today().isoformat())
    )


def _get_active_modules(config_path: Path) -> list[str]:
    """Return the list of active modules from config.md."""
    if not config_path.exists():
        return []
    text = config_path.read_text("utf-8")
    match = re.search(r"^active_modules:(.*?)(?=\n\S|\Z)", text, re.MULTILINE | re.DOTALL)
    if not match:
        return []
    return re.findall(r"^\s*-\s+(.+)$", match.group(1), re.MULTILINE)


def _set_active_modules(config_path: Path, modules: list[str]) -> None:
    """Rewrite the active_modules block in config.md."""
    text = config_path.read_text("utf-8")
    if modules:
        items = "\n".join(f"  - {m}" for m in modules)
        new_block = f"active_modules:\n{items}"
    else:
        new_block = "active_modules: []"
    if "active_modules:" in text:
        text = re.sub(
            r"^active_modules:.*?(?=\n\S|\Z)",
            new_block,
            text,
            flags=re.MULTILINE | re.DOTALL,
        )
    else:
        text = text.rstrip() + f"\n\n{new_block}\n"
    config_path.write_text(text, "utf-8")


@click.group()
@click.version_option(package_name="business-kit")
def cli() -> None:
    """business-kit — spec-driven business development.

    Run 'bk init' to scaffold a new project, then open brief.md
    and invoke /bk.brief in your AI assistant to get started.
    """


@cli.command()
@click.option(
    "--type",
    "project_type",
    type=click.Choice(["gtm", "partnership", "pitch", "strategy", "general"]),
    default="general",
    show_default=True,
    help="Pre-populate templates for a specific business motion.",
)
@click.option(
    "--name",
    "project_name",
    default=None,
    help="Project name (defaults to current directory name).",
)
def init(project_type: str, project_name: str | None) -> None:
    """Scaffold .businesskit/ folder and artifact files in the current directory."""
    root = Path.cwd()
    if project_name is None:
        project_name = root.name

    bk_dir = root / ".businesskit"
    commands_dir = bk_dir / "commands"
    execute_dir = root / "execute"

    for d in (bk_dir, commands_dir, execute_dir):
        d.mkdir(parents=True, exist_ok=True)

    created: list[str] = []
    skipped: list[str] = []

    def _track(path: Path, wrote: bool) -> None:
        rel = str(path.relative_to(root))
        (created if wrote else skipped).append(rel)

    # .businesskit/config.md — rendered with project metadata
    config_path = bk_dir / "config.md"
    _track(config_path, _write_if_new(config_path, _render_config(project_type, project_name)))

    # .businesskit/constitution.md and glossary.md
    for name in ("constitution.md", "glossary.md"):
        dst = bk_dir / name
        _track(dst, _write_if_new(dst, (TEMPLATES_DIR / name).read_text("utf-8")))

    # .businesskit/commands/ — one instruction file per slash command
    for src in sorted((TEMPLATES_DIR / "commands").iterdir()):
        dst = commands_dir / src.name
        _track(dst, _write_if_new(dst, src.read_text("utf-8")))

    # brief.md — preset-specific template
    brief_src = TEMPLATES_DIR / "brief" / f"brief.{project_type}.md"
    brief_dst = root / "brief.md"
    _track(brief_dst, _write_if_new(brief_dst, brief_src.read_text("utf-8")))

    # strategy.md and plan.md
    for artifact in ("strategy", "plan"):
        src = TEMPLATES_DIR / f"{artifact}.template.md"
        dst = root / f"{artifact}.md"
        _track(dst, _write_if_new(dst, src.read_text("utf-8")))

    # execute/ assets for the chosen preset
    execute_assets = PRESET_EXECUTE_ASSETS[project_type]
    for asset in execute_assets:
        src = TEMPLATES_DIR / "execute" / f"{asset}.md"
        dst = execute_dir / f"{asset}.md"
        _track(dst, _write_if_new(dst, src.read_text("utf-8")))

    # .gitkeep to track an otherwise empty execute/ directory
    if not execute_assets:
        gitkeep = execute_dir / ".gitkeep"
        if not gitkeep.exists() and not any(execute_dir.iterdir()):
            gitkeep.touch()
            created.append("execute/.gitkeep")

    # ── Output ──────────────────────────────────────────────────────────────
    click.echo()
    click.secho("  business-kit initialized", fg="green", bold=True)
    click.echo(f"  Project : {project_name}")
    click.echo(f"  Type    : {project_type}")

    if created:
        click.echo()
        click.secho("  Created:", fg="cyan")
        for f in created:
            click.echo(f"    + {f}")

    if skipped:
        click.echo()
        click.secho("  Already exist (skipped):", fg="yellow")
        for f in skipped:
            click.echo(f"    ~ {f}")

    click.echo()
    click.secho("  Next steps:", bold=True)
    click.echo("    1. Edit  .businesskit/constitution.md  — set tone, brand, non-negotiables")
    click.echo("    2. Open  brief.md  in your editor")
    click.echo("    3. In your AI assistant, run:  /bk.brief")
    click.echo()


# ── Module commands ──────────────────────────────────────────────────────────

@cli.group()
def module() -> None:  # noqa: A001
    """Manage optional framework modules."""


@module.command("add")
@click.argument("name")
def module_add(name: str) -> None:
    """Install a module into .businesskit/modules/."""
    root = Path.cwd()
    bk_dir = root / ".businesskit"

    if not bk_dir.exists():
        click.secho("  Error: no .businesskit/ directory found.", fg="red")
        click.echo("  Run 'bk init' first.")
        raise SystemExit(1)

    if name not in AVAILABLE_MODULES:
        click.secho(f"  Error: '{name}' is not a recognised module.", fg="red")
        click.echo(f"  Available: {', '.join(AVAILABLE_MODULES)}")
        raise SystemExit(1)

    config_path = bk_dir / "config.md"
    active = _get_active_modules(config_path)

    if name in active:
        click.secho(f"  '{name}' is already active.", fg="yellow")
        return

    # Conflict check — rfp-issue and rfp-respond serve opposite roles
    for a, b in CONFLICTING_PAIRS:
        if name in (a, b):
            other = b if name == a else a
            if other in active:
                click.secho(
                    f"  Warning: '{name}' and '{other}' serve opposite roles (buyer vs vendor).",
                    fg="yellow",
                    bold=True,
                )
                click.echo("  Using both in the same project is unusual — consider separate projects.")
                if not click.confirm("  Continue anyway?", default=False):
                    raise SystemExit(0)

    # Copy module folder from templates into .businesskit/modules/
    src = MODULES_DIR / name
    dst = bk_dir / "modules" / name
    dst.parent.mkdir(parents=True, exist_ok=True)
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst)

    # Update active_modules in config.md
    _set_active_modules(config_path, active + [name])

    click.echo()
    click.secho(f"  Module '{name}' installed", fg="green", bold=True)
    click.echo(f"  Location: .businesskit/modules/{name}/")
    commands = MODULE_COMMANDS.get(name, [])
    if commands:
        click.echo()
        click.secho("  New commands:", fg="cyan")
        for cmd in commands:
            click.echo(f"    {cmd}")
    click.echo()


@module.command("list")
def module_list() -> None:
    """Show available modules and their status."""
    root = Path.cwd()
    bk_dir = root / ".businesskit"
    config_path = bk_dir / "config.md"

    if bk_dir.exists():
        active = _get_active_modules(config_path)
    else:
        active = []
        click.secho("  (No .businesskit/ found — run 'bk init' first)", fg="yellow")

    click.echo()
    click.secho("  Available modules:", bold=True)
    click.echo()
    for mod in AVAILABLE_MODULES:
        if mod in active:
            marker = click.style("active", fg="green")
        else:
            marker = click.style("      ", fg="white")  # spacing placeholder
        desc = MODULE_DESCRIPTIONS.get(mod, mod)
        cmds = "  →  " + ", ".join(MODULE_COMMANDS.get(mod, []))
        click.echo(f"    [{marker}]  {mod:<16}  {desc}")
        if mod in active:
            click.echo(f"               {' ' * 16}  {cmds}")
    click.echo()


@module.command("remove")
@click.argument("name")
def module_remove(name: str) -> None:
    """Deactivate a module. Files in .businesskit/modules/ are kept."""
    root = Path.cwd()
    bk_dir = root / ".businesskit"

    if not bk_dir.exists():
        click.secho("  Error: no .businesskit/ directory found.", fg="red")
        raise SystemExit(1)

    config_path = bk_dir / "config.md"
    active = _get_active_modules(config_path)

    if name not in active:
        click.secho(f"  '{name}' is not currently active.", fg="yellow")
        return

    _set_active_modules(config_path, [m for m in active if m != name])

    click.echo()
    click.secho(f"  Module '{name}' deactivated", fg="yellow", bold=True)
    click.echo(f"  Files in .businesskit/modules/{name}/ have been kept.")
    click.echo()
