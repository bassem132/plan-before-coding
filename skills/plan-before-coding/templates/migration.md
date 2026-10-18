# Plan: migrate <from> → <to>

## Why now
<The reason, e.g. "v2 is end-of-life in March".>

## Inventory
- Usages found: <count> in <files> (`grep -rn <pattern>`)
- Data affected: <tables / files / none>

## Rollback
<How to undo each step. If a step can't be undone, mark it ⚠️ and get explicit approval before running it.>

## Steps
1. Add <to> alongside <from> (both work) — check: build + tests pass.
2. Move usages in batches of ~<n> files — check: tests pass after each batch.
3. ⚠️ Data migration: <what> — check: dry run on a copy; row counts match before/after.
4. Remove <from> — check: no references left; tests pass.

## Out of scope
- <...>
