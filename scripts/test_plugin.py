#!/usr/bin/env python3
"""Structural checks for the wstack Cursor plugin."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

EXPECTED_FILES = {
    ".cursor-plugin/plugin.json",
    ".gitignore",
    "LICENSE",
    "README.md",
    "scripts/test_plugin.py",
    "skills/setup-wstack/SKILL.md",
    "skills/wstack/SKILL.md",
    "skills/wstack/playbooks/investigation.md",
    "skills/wstack/playbooks/authoring-a-skill.md",
    "skills/wstack/playbooks/work.md",
    "skills/how/SKILL.md",
    "skills/how/references/critic-prompt.md",
    "skills/how/references/critique-rubric.md",
    "skills/how/references/explainer-prompt.md",
    "skills/how/references/explorer-prompt.md",
    "skills/why/SKILL.md",
    "skills/why/references/epistemics.md",
    "skills/why/references/investigator-prompt.md",
    "skills/why/references/source-playbook.md",
    "skills/why/references/synthesizer-prompt.md",
    "skills/why/references/sources/code-archaeology.md",
    "skills/why/references/sources/databricks.md",
    "skills/why/references/sources/datadog.md",
    "skills/why/references/sources/github-issues.md",
    "skills/why/references/sources/incident-postmortem.md",
    "skills/why/references/sources/repo-docs.md",
    "skills/teach/SKILL.md",
    "skills/recall/SKILL.md",
}

SETUP_ROLES = [
    "how explorer",
    "how explainer",
    "how critics",
    "why investigators",
    "why synthesizer",
]

GHOST_ROLES = [
    "judgment and prose",
    "hardest tasks",
    "arena runners",
    "architect runners",
]

FORBIDDEN_SOURCE_WORDS = ("Linear", "Notion", "Sentry", "Slack")
PERSONAL = (
    "Drew You",
    "Lauren Tan",
    "drawnwren@",
    "Co-authored-by",
    "pstack",
    "poteto",
)
EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
ALLOWED_EMAIL_CONTEXT = ()


def fail(msg: str) -> None:
    print(f"FAIL: {msg}", file=sys.stderr)
    raise SystemExit(1)


def tracked_files() -> list[Path]:
    files = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(ROOT).as_posix()
        if rel.startswith(".git/"):
            continue
        files.append(path)
    return files


def main() -> None:
    rels = {p.relative_to(ROOT).as_posix() for p in tracked_files()}
    extra = rels - EXPECTED_FILES
    missing = EXPECTED_FILES - rels
    if extra:
        fail(f"unexpected files: {sorted(extra)}")
    if missing:
        fail(f"missing files: {sorted(missing)}")
    if len(rels) != 28:
        fail(f"expected 28 files, found {len(rels)}")

    if (ROOT / "agents").exists():
        fail("agents/ directory must not exist")

    sha = list(ROOT.glob("scripts/*.sha256")) + list(ROOT.glob("checksum/*.sha256"))
    if sha:
        fail(f"checksum lockfiles present: {sha}")

    manifest_path = ROOT / ".cursor-plugin" / "plugin.json"
    manifest = json.loads(manifest_path.read_text())
    if manifest.get("name") != "wstack":
        fail("plugin.json name must be wstack")
    if "author" in manifest:
        fail("plugin.json must not have an author field")
    if "agents" in manifest:
        fail("plugin.json must not declare agents")

    license_text = (ROOT / "LICENSE").read_text()
    if "MIT License" not in license_text:
        fail("LICENSE must be MIT")
    if "Copyright (c) 2026" not in license_text:
        fail("LICENSE must include Copyright (c) 2026")
    if re.search(r"Copyright \(c\) 2026 .+", license_text):
        fail("LICENSE copyright must not include a personal name")

    setup = (ROOT / "skills/setup-wstack/SKILL.md").read_text()
    for role in SETUP_ROLES:
        if f"{role}:" not in setup:
            fail(f"setup-wstack missing role {role!r}")
    for ghost in GHOST_ROLES:
        if ghost in setup:
            fail(f"setup-wstack contains ghost role {ghost!r}")
    if "alwaysApply: true" not in setup:
        fail("setup-wstack must write alwaysApply: true")
    if "inherit-parent" not in setup or "`auto`" not in setup and "auto" not in setup:
        fail("setup-wstack must allow inherit-parent and auto")

    wstack = (ROOT / "skills/wstack/SKILL.md").read_text()
    front = wstack.split("---", 2)[1]
    for needle in (
        "name: wstack",
        "disable-model-invocation: true",
        "mode: true",
        "icon: globe",
        "color: blue",
    ):
        if needle not in front:
            fail(f"sticky /wstack missing {needle!r}")
    if "skip: <reason>" not in wstack and "skip: <reason>" not in wstack.replace("`", ""):
        if "skip: <reason>" not in wstack:
            fail("wstack must require skip: <reason>")
    if "playbooks/investigation.md" not in wstack:
        fail("wstack missing investigation playbook")
    if "should we do X or Y" not in wstack:
        fail("investigation match must include should we do X or Y")
    if "Do not load extra playbooks from another plugin unless the user says to." not in wstack:
        fail("wstack must not load extra playbooks unless asked")

    investigation = (ROOT / "skills/wstack/playbooks/investigation.md").read_text()
    if "should we do X or Y" not in investigation:
        fail("investigation playbook must include should we do X or Y")
    if "No PR unless asked" not in investigation:
        fail("investigation must not open a PR unless asked")

    authoring = (ROOT / "skills/wstack/playbooks/authoring-a-skill.md").read_text()
    if "create-skill" not in authoring:
        fail("authoring playbook must use create-skill")
    if "python3 scripts/test_plugin.py" not in authoring:
        fail("authoring playbook must run python3 scripts/test_plugin.py")
    if "*.sha256" not in authoring:
        fail("authoring playbook must forbid hash lockfiles")

    work = (ROOT / "skills/wstack/playbooks/work.md").read_text()
    for missing_skill in (
        "architect",
        "arena",
        "swarm",
        "interrogate",
        "tdd",
        "unslop",
        "no-comments",
    ):
        if missing_skill not in work:
            fail(f"work playbook must keep {missing_skill} as skip: not shipped")
    if "skip: not shipped" not in work:
        fail("work playbook must use skip: not shipped")
    if "still unshipped" not in work:
        fail("work reply must include what is still unshipped in wstack")

    for skill in ("how", "why", "teach", "recall"):
        if not (ROOT / "skills" / skill / "SKILL.md").is_file():
            fail(f"missing skills/{skill}/SKILL.md")

    why = (ROOT / "skills/why/SKILL.md").read_text()
    for required in (
        "git",
        "GitHub Issues",
        "markdown",
        "Datadog",
        "warehouse",
    ):
        if required not in why:
            fail(f"/why must mention {required}")

    teach = (ROOT / "skills/teach/SKILL.md").read_text()
    if "**unslop**" not in teach and "unslop" not in teach:
        fail("teach must still name unslop")
    if "skip: not shipped" not in teach:
        fail("teach must skip unslop as not shipped")

    recall = (ROOT / "skills/recall/SKILL.md").read_text()
    if "unslop" not in recall:
        fail("recall must still name unslop")
    if "skip: not shipped" not in recall:
        fail("recall must skip unslop as not shipped")

    sources_dir = ROOT / "skills/why/references/sources"
    source_names = sorted(p.name for p in sources_dir.glob("*.md"))
    expected_sources = [
        "code-archaeology.md",
        "databricks.md",
        "datadog.md",
        "github-issues.md",
        "incident-postmortem.md",
        "repo-docs.md",
    ]
    if source_names != expected_sources:
        fail(f"why sources {source_names} != {expected_sources}")

    skip_self = "scripts/test_plugin.py"
    for path in tracked_files():
        rel = path.relative_to(ROOT).as_posix()
        text = path.read_text(errors="replace")
        if rel != skip_self:
            for word in FORBIDDEN_SOURCE_WORDS:
                if word in text:
                    fail(f"{rel} contains omitted source {word!r}")
            for needle in PERSONAL:
                if needle in text:
                    fail(f"{rel} contains forbidden provenance {needle!r}")
        for match in EMAIL_RE.findall(text):
            fail(f"{rel} contains email {match!r}")

    print("ok: 28 files, wstack plugin checks passed")


if __name__ == "__main__":
    main()
