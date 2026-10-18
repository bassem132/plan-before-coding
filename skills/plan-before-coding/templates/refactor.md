# Plan: refactor <area>

## Why
<The concrete problem: duplication, a bug class, something hard to change. "Cleaner" is not a reason.>

## Behaviour that must not change
- <Public API, outputs, performance budget, URLs…>

## Safety net
- Existing tests covering this: <paths / "none — step 1 adds them">

## Steps
1. Add characterization tests for current behaviour — check: they pass on the old code.
2. <Mechanical change, e.g. extract function> — check: all tests still pass.
3. <Next small change> — check: all tests still pass.
4. Remove the old code path — check: tests pass, no references left (`grep -r <old name>`).

## Rules for this plan
- Every step leaves the code working and tests green.
- No behaviour changes mixed into refactor steps. If one is needed, make it its own step and say so.

## Out of scope
- <...>
