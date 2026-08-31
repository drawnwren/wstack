---
name: setup-wstack
description: Configure which models wstack uses per role. Detects your available models and writes an always-applied rule that overrides the how and why skill defaults. Use for /setup-wstack, "configure wstack models", or changing wstack's model choices.
---

# Setup wstack

Write `~/.cursor/rules/wstack-models.mdc`, an always-applied rule that sets wstack's model per role. The how and why skills read it and fall back to their inline defaults when a line is absent, so this is an override layer, not a requirement. Playbook delegates omit Task `model` and inherit the parent chat.

## Steps

### 1. Detect available models

Enumerate the model slugs you can pass to a `Task` subagent in this session; that is the dependable source. If Cursor also exposes a models API or CLI that lists the user's entitled models, prefer it for completeness. If you cannot detect any, ask the user to paste the slugs they have access to. Never write a real slug you have not confirmed is available. The aliases `inherit-parent` and `auto` are always valid even though they are not detected slugs. Both mean: omit Task `model` so the role runs on the parent chat model.

### 2. Load current state

The default role-to-model mapping is the rule shape shown in step 5 below. If `~/.cursor/rules/wstack-models.mdc` already exists, read it and treat its values as the current choices. Otherwise start from those defaults.

### 3. Map and confirm

Show every role with its current model, marking any real slug not in the detected set as needing a choice. Ask whether to accept as-is or change specific roles, offering the detected models plus `inherit-parent` and `auto` as the options. Prefer AskQuestion over free text. Role keys use spaces (`how explorer`, not `how-explorer`). `how critics` is a list, and one subagent runs per entry, alias entries included, so the list length sets the count.

Do not invent extra roles. The file has five roles only.

### 4. Validate

Every real slug written must be in the detected set; `inherit-parent` and `auto` always pass. If a chosen real slug is not available, stop and ask again. A rule pointing at a model the user cannot use breaks every delegation that reads it.

### 5. Write the rule

Write `~/.cursor/rules/wstack-models.mdc` with `alwaysApply: true` and one line per role. Overwrite the whole file so re-runs stay idempotent. Shape:

```
---
description: wstack per-role model choices (overrides skill defaults)
alwaysApply: true
---
# wstack model configuration. One line per role. Delete a line to fall back to the skill default.
# `inherit-parent` or `auto` as a value: the role runs on the parent chat model (omit Task `model`). Alias entries in a panel list still count toward its fan-out.
how explorer: grok-4.6-fast-xhigh
how explainer: claude-fable-5-thinking-max
how critics: claude-fable-5-thinking-max, gpt-5.6-sol-max, grok-4.6-fast-xhigh, claude-opus-5-thinking-xhigh
why investigators: grok-4.6-fast-xhigh
why synthesizer: claude-fable-5-thinking-max
```

### 6. Confirm

Tell the user the rule was written and that it applies to new sessions. Re-running this skill updates it. Start a new chat so the rule is loaded.
