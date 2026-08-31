### Work

**You own the change. Plan, edit, verify.**

Any other change to code or docs. Understand first, then change.

1. Run the **how** skill over the affected subsystem when the change is nontrivial. Motivation questions also run **why**.
2. Name the data shape and the smallest change that works.
3. Keep these steps in the todolist even though the skills are missing. Mark each `skip: not shipped` and continue:
   - **architect**
   - **arena**
   - **swarm**
   - **interrogate**
   - **tdd**
   - **unslop**
   - **no-comments**
4. Implement. Spawn playbook delegates as `generalPurpose`. Omit Task `model` so they inherit the parent chat.
5. Verify with the closest real check (tests, a script, a build). "Inconclusive" is not a pass.
6. Open a PR when the user wants one. Do not add checksum lockfiles or `*.sha256` sidecars.

**Reply:** what you built, how you verified, open decisions, and what is still unshipped in wstack (architect, arena, swarm, interrogate, tdd, unslop, no-comments).
