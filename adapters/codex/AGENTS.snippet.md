<!-- plan-before-coding by Bassem Moumen (MIT). Paste into your AGENTS.md if you don't install the full skill. -->

## Plan before coding

- For features, refactors, migrations or any change touching 2+ files, write a short plan before editing code. Wait for my go-ahead only if it touches 3+ files, has a risky step, or the request is ambiguous; otherwise state a 3–5 line plan and proceed.
- Plan = Goal, Assumptions, at most 3 open questions (each with a default), numbered Steps, Out of scope.
- Every step names the files it touches and ends with `check:` (a test, command or visible result). "Looks good" is not a check.
- Mark risky steps (data, auth, money, public APIs, deletes) with ⚠️ and do them early.
- If reality doesn't match the plan, stop and tell me what changed before continuing.
