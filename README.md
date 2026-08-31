# wstack

Understand first, then change.

Install from GitHub. Cursor indexes this repo as a marketplace via `.cursor-plugin/marketplace.json`. A repo with only `.cursor-plugin/plugin.json` is a single plugin, not a marketplace, so `/add-plugin` and **Import from Repo** both miss it.

Agent chat:

```text
/add-plugin wstack@https://github.com/drawnwren/wstack
```

Or paste `https://github.com/drawnwren/wstack` into Customize -> Plugins -> add from GitHub / Dashboard -> Plugins -> Import from Repo.

Local checkout for development: `~/.cursor/plugins/local/wstack`. The plugin root is this git root.

## Doors

1. `/setup-wstack` writes `~/.cursor/rules/wstack-models.mdc` with five roles: how explorer, how explainer, how critics, why investigators, why synthesizer.
2. `/wstack` is the sticky mode. Match a playbook, copy its steps into todos, and keep `skip: <reason>` instead of silent skips.

## What ships now

| Skill | Use |
|---|---|
| `/how` | How a subsystem works. Optional critique. |
| `/why` | Why it was built this way. Five evidence categories. |
| `/teach` | how + why, explained plainly. Names unslop; that skill is not shipped. |
| `/recall` | Rebuild recent working context. Same unslop skip. |

## `/wstack` playbooks

- Investigation. Read-only, including "should we do X or Y?"
- Authoring or modifying a skill.
- Work. Any other change to code or docs.

## `/why` sources

git/gh. GitHub Issues via `gh`. In-repo markdown. Datadog-style observability. Product analytics warehouse.

## License

MIT. Copyright (c) 2026.
