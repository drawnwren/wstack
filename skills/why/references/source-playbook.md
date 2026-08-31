# Source playbooks

The why skill spawns one investigator per available evidence category, each reading a single source-specific playbook below.

| Category | Playbook | Tools it documents |
|---|---|---|
| Source control history | [`code-archaeology.md`](./sources/code-archaeology.md) | git, `gh` |
| GitHub Issues | [`github-issues.md`](./sources/github-issues.md) | `gh issue`, `gh search issues` |
| In-repo markdown | [`repo-docs.md`](./sources/repo-docs.md) | README, `docs/`, ADRs, RFCs in the tree |
| Infrastructure observability | [`datadog.md`](./sources/datadog.md) | Datadog-style MCP |
| Product analytics warehouse | [`databricks.md`](./sources/databricks.md) | Databricks-style SQL MCP |

Cross-cutting:

- [`incident-postmortem.md`](./sources/incident-postmortem.md). Add this if the target code looks defensive (null checks, retry, timeout, rate limit, feature flag, egress guard, OOM handler).
