# Incident & Postmortem Context

Not a separate source, a **cross-cutting angle**. Incidents often motivate defensive code ("we added this check after the X outage"), so if the target looks defensive (null checks, retry logic, timeout handling, rate limiting, feature flags), specifically hunt for incident history across every available source:

- **Git**: commits with messages like "fix for incident", "add defensive check", "revert" followed by "re-apply with..." are strong signals
- **GitHub Issues**: look for issues labeled `incident`, `sev-*`, `postmortem-action-item`, `reliability`
- **In-repo markdown**: search `docs/` for postmortems mentioning the target file, feature, or error string
- **Datadog-style observability**: formal incident records with timelines; dashboards and monitors created as postmortem action items
- **Databricks-style warehouse**: product-analytics events that classify an error condition often spike during an incident window. A drop in that event count after the target PR ships is circumstantial support that the target code resolved the user-visible symptom

If you find an incident link, fetch the full postmortem. Postmortems typically have an "Action Items" section that ties directly to code changes. When multiple sources corroborate (a Datadog incident ID appears in a GitHub issue, which appears in a repo postmortem that links to the target PR, and the warehouse error-event count drops after the fix), the evidence is especially strong.

Worth spending time on when the code's defensive character makes an incident-driven origin plausible. Skip it for code that doesn't look defensive.
