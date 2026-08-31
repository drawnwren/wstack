### Authoring or modifying a skill

**You own the skill's voice.** Agent-facing prose has a higher bar than human prose; unhelpful sentences become instructions.

1. Use the **create-skill** skill (Cursor's built-in for authoring SKILL.md files).
2. Validate the skill: frontmatter has `name` and `description`, referenced files exist, cross-skill links resolve.
3. Run `python3 scripts/test_plugin.py`.
4. Test cases if structural; skip if subjective. Keep `skip: <reason>` when you skip.
5. Open a PR if asked. Do not add checksum lockfiles, hash manifests, or `*.sha256` sidecars. Git already records file contents.

When in doubt, delete; prose earns its keep by changing a decision. Tell it to do the thing and skip the reason. Explain only when the rule is confusing without one. Match tone to scope. Point at structural sources (types, READMEs, config); hardcoded details go stale. Delegate to other skills by path; don't restate.

Playbook delegates omit Task `model`.

**Reply:** summary of the skill, key design decisions, validation notes, and the test command result.
