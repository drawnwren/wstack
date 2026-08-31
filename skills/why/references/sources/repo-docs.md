# In-repo markdown

## What this source contains

Long-form rationale that already lives in the git tree:

- README and contributing guides
- `docs/` (guides, RFCs, design notes)
- ADRs (`docs/adr/`, `adr/`, `ARCHITECTURE.md`)
- In-tree postmortems and runbooks
- Changelog and release notes when they explain why, not only what

This is the long-form category. Search the repository's markdown, not an external wiki.

## How to search it

```bash
# Likely docs
rg -l -i '<feature or symbol>' --glob '*.md'

# ADRs
rg -l -i 'architecture.decision|adr' --glob '*.md'

# Design / RFC language
rg -n -i 'alternatives considered|we chose|rejected|rationale' --glob '*.md'
```

Read matching files fully. Titles lie; the useful paragraph is often under "Motivation" or "Alternatives".

1. **Start at paths named in the seed commits.** A PR that adds `docs/retry.md` is a direct lead.
2. **Walk `docs/` and README sections** that name the subsystem.
3. **Read ADRs** even when they look stale. A superseded ADR still records the original why.
4. **Stay in markdown.** Inline code comments belong to the source-control investigator.

## What good evidence looks like here

- An ADR that names the option taken and the options rejected
- A README "Why" or "Design" section that states the constraint
- An RFC with an explicit tradeoff table
- A postmortem checked into `docs/` whose action items name the target

## Common pitfalls

- **Docs drift.** A README can describe a design that shipped two rewrites ago. Date it against git history.
- **Aspirational docs.** "We will" is not evidence of what shipped.
- **Duplicated ADRs.** Prefer the one linked from the PR or the one in the same directory as the code.

## What to return

Every markdown passage that bears on the question, with:
- Quoted text
- File path and heading
- Commit that last changed that section, if you can get it cheaply
- Direct vs circumstantial
