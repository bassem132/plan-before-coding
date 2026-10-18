---
name: plan-before-coding
description: Turn a feature request into a short written plan of small, verifiable steps before writing any code. Use when a task touches more than one file, adds a feature, changes behaviour, or the request is ambiguous. Skip for one-line fixes.
author: Bassem Mo'men
license: MIT
---

# Plan before coding

Most wasted agent work comes from building the wrong thing confidently. Five minutes of planning saves an hour of rework, and a written plan lets the user correct course before any code exists.

## When to use

- New features, refactors, migrations, anything touching 2+ files.
- The request has more than one reasonable interpretation.
- You'd need to guess at a library, data shape, API or UX detail.

Skip it for typos, one-line fixes and tasks the user already spelled out step by step.

## Procedure

1. **Read before you plan.** Find the files, patterns and tests the change will touch. Note how similar features are already built — follow them.
2. **Restate the goal** in one or two sentences, including what "done" looks like from the user's side.
3. **List assumptions and open questions.** Ask only the questions whose answer changes the plan (max 3). For everything else, pick the conventional default and write it down as an assumption.
4. **Write the plan** as numbered steps. Each step:
   - changes one coherent thing,
   - names the files it touches,
   - ends with a check: a test, a command, or something visible.
5. **Mark the risky step** — the one most likely to be wrong (data migration, auth, payments, public API). Plan to do it early or behind a check.
6. **Get a go-ahead** on the plan, then execute it step by step. After each step, run its check before moving on.
7. **If reality disagrees with the plan**, stop, update the plan, and tell the user what changed and why. Don't silently drift.

## Plan format

```markdown
## Goal
Users can export invoices as PDF from the invoice page.

## Assumptions
- Use the existing `pdfkit` dependency (already in package.json).
- Export is one invoice at a time; bulk export is out of scope.

## Steps
1. Add `renderInvoicePdf(invoice)` in src/invoices/pdf.ts — check: unit test renders a sample invoice without throwing.
2. Add GET /invoices/:id/pdf route in src/routes/invoices.ts — check: curl returns application/pdf. ⚠️ risky: permission check.
3. Add "Download PDF" button to InvoicePage.tsx — check: click downloads the file in the dev server.

## Out of scope
- Email delivery, bulk export.
```

## Rules

- Small steps beat big ones: if a step's check would fail for five different reasons, split it.
- No step without a check. "Looks good" is not a check.
- Write "Out of scope" explicitly — it prevents scope creep.
- Keep the plan short enough to read in one minute.
