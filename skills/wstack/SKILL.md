---
name: wstack
description: Understand first, then change. Use for /wstack, wstack-mode, or requests to work in this style.
disable-model-invocation: true
mode: true
icon: globe
color: blue
reminder: New task? Playbook match or rigor needed -> apply /wstack. Casual turn or user opts out -> don't.
---
# wstack
Sticky mode. On entry, read this file in full. Later turns get the reminder line, not another full inject. Re-apply on a new task when a playbook matches or the work needs rigor. Stand down on casual turns and when the user opts out.
## Non-negotiables
Start every multi-step task with a todolist. Match a playbook from the Playbooks section, then copy that playbook's steps in verbatim as the first todos. A step you do not do stays in the list as `skip: <reason>`. Silent skips are not allowed.
Remaining triggers:
- Nontrivial change, architecture question, or "are we sure?" → the **how** skill.
- Motivation, history, or "why is it like this?" → the **why** skill.
- The human wants to actually understand it → the **teach** skill. teach names **unslop**. That skill is not in this plugin. Keep `skip: not shipped` for unslop and write the explanation in short sentences anyway.
- Starting or resuming work cold → the **recall** skill. Same unslop skip.
- Code change with no more specific playbook → **Work** (`playbooks/work.md`).
- Writing or editing a SKILL.md → **Authoring or modifying a skill** (`playbooks/authoring-a-skill.md`).
- A named skill that is not in this plugin yet → keep the step, mark `skip: not shipped`, continue. Do not stall and do not fake the missing skill.
- Before a PR: do not add checksum lockfiles, hash manifests, or byte-pin sidecars (`*.sha256` next to skills, and the like). Git already records file contents. A test may check that a skill exists. It may not re-hash the tree.
## Models
Read `~/.cursor/rules/wstack-models.mdc` when it exists. `/setup-wstack` writes it. That file only overrides `/how` and `/why`. Playbook delegates omit Task `model` and inherit the parent chat until a later skill adds a role line. `inherit-parent` and `auto` mean the same omit. Role keys use spaces (`how explorer`, not `how-explorer`). When you add a new skill, add its line in the same change.
Spawn playbook delegates as `generalPurpose` unless a later `wstack-agent` file exists. Routed skills (`how`, `why`) set their own `subagent_type`. Do not override those.
## Writing
Short declarative sentences. One thought per sentence. No em dashes. No colon used as a mid-sentence connector. No chatbot closers. Name who the work is for before implementation detail.
## Playbooks
Match the task, open the playbook file, copy its steps into the todolist before any task-specific todos.
- **Investigation.** Read-only question: how does X work, why was Y built this way, are we sure about Z, should we do X or Y. `playbooks/investigation.md`.
- **Authoring or modifying a skill.** Writing or editing a SKILL.md. `playbooks/authoring-a-skill.md`.
- **Work.** Any other change to code or docs. `playbooks/work.md`.
That is the whole set on purpose. Do not load extra playbooks from another plugin unless the user says to.
