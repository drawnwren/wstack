# GitHub Issues

## What this source contains

- Issues describing features, bugs, and their motivation
- Comments on issues (clarifications, scope changes, rationale)
- Labels that signal the type of motivation
- Linked pull requests (`closingIssuesReferences`, "Fixes #N")
- Project or milestone framing when the repo uses it

GitHub Issues is where the product or business context often lives when the team tracks work on GitHub: the "we're doing this because of X" layer.

## How to search it

Use `gh`. Do not invent a second issue tracker.

```bash
# Linked issues from the seed PRs
gh pr view <number> --json closingIssuesReferences,body

# Fetch a known issue, including comments
gh issue view <number> --comments

# Keyword search in this repo
gh issue list --search "<feature or symbol>" --state all --limit 50

# Cross-repo search when the org uses one issues repo
gh search issues "<feature or symbol>" --repo <owner>/<repo> --limit 50
```

1. **Start with linked issues.** If seed commits or PRs reference `#1234`, fetch those first. Read the full issue including comments.
2. **List related issues by keyword.** Search for the feature name, key symbol, or business term. Try multiple phrasings.
3. **Walk parents and duplicates.** Follow "blocked by", "duplicate of", and tracking-issue links. Sub-issues are tactical; tracking issues often carry the why.
4. **Check labels and milestones.** Labels hint at the category of motivation. Milestones tie work to deadlines.

## What good evidence looks like here

- An issue description stating the business problem
- A comment recording a decision
- A tracking issue titled like an initiative
- Labels like `customer-request`, `incident-followup`, `compliance`, `perf-regression`

## Common pitfalls

- **Scope drift.** The issue the PR closes may have been rewritten. Read the whole comment history.
- **Mechanical templates.** Generic text ("improve user experience") is probably not a real answer.
- **Stale issues.** Old issues often reflect a plan that changed. Check dates against the code's ship date.
- **Closed-as-duplicate chains.** Follow them back to the canonical issue.

## What to return

Every issue/comment that bears on the question, with:
- The exact text (quoted)
- The issue number and URL
- Author and date
- Whether it's direct or circumstantial
