# Plan: fix <bug>

## Symptom
<What the user sees. Exact error message if there is one.>

## Reproduction
<Command, test or click path that fails every time.>

## Suspected cause
<Best hypothesis, and what evidence points to it. If unknown, step 1 is finding it — see the debug-root-cause skill.>

## Steps
1. Write a failing test that reproduces the bug in `<file>` — check: test fails for the right reason.
2. Fix the cause in `<file>` — check: new test passes.
3. Run the full suite — check: `<test command>` all green.

## Out of scope
- <Nearby problems noticed but not fixed now — list them so they aren't lost.>
