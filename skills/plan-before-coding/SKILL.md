---
name: plan-before-coding
description: Turn a request into a short written plan of small, checkable steps before writing code, and get a go-ahead first. Use when the user asks to build, add, implement, refactor, migrate or redesign something; when a change touches more than one file; when the request could mean more than one thing; or when you'd have to guess a library, data shape or UX detail. Skip it for typos, one-line fixes and tasks the user already spelled out step by step.
author: Bassem Mo'men
license: MIT
---

# Plan before coding

Most wasted agent work comes from building the wrong thing with confidence. A few minutes of planning saves an hour of rework, and a written plan lets the user correct course before any code exists.

## When to use

- New features, refactors, migrations, or anything touching 2+ files.
- The request could reasonably mean more than one thing.
- You'd have to guess a library, data shape, API or UX detail.

Skip it for typos, one-line fixes and tasks the user already wrote out step by step.

## Procedure

1. **Read before you plan.** Find the files, patterns and tests the change will touch. Note how similar features are built already, and follow that pattern.
2. **Pick a template** from `templates/`: [feature](templates/feature.md), [bugfix](templates/bugfix.md), [refactor](templates/refactor.md) or [migration](templates/migration.md).
3. **Restate the goal** in one or two sentences, including what "done" looks like for the user.
4. **List assumptions and open questions.** Ask only questions whose answer changes the plan, three at most, each with a default. For everything else, choose the conventional option and write it down as an assumption. See [reference/good-questions.md](reference/good-questions.md).
5. **Write the steps.** Each step:
   - changes one coherent thing,
   - names the files it touches,
   - ends with `check:`, meaning a test, a command, or a result you can see.
6. **Mark risky steps with ⚠️**, such as data, auth, money, public APIs or deletes. Do them early or behind a check. See [reference/risky-steps.md](reference/risky-steps.md).
7. **Lint the plan** before showing it:
   ```bash
   python3 <skill-dir>/scripts/check_plan.py plan.md     # or pipe it in: … check_plan.py -
   ```
8. **Get a go-ahead**, then work through the steps in order. After each step, run its check before starting the next.
9. **If reality doesn't match the plan**, stop, update the plan, and tell the user what changed and why. Don't drift silently.

## Plan format

```markdown
## Goal
Users can export invoices as PDF from the invoice page.

## Assumptions
- Use the existing `pdfkit` dependency (already in package.json).
- One invoice at a time; bulk export is out of scope.

## Steps
1. Add `renderInvoicePdf(invoice)` in `src/invoices/pdf.ts` — check: unit test renders a sample invoice.
2. Add GET /invoices/:id/pdf in `src/routes/invoices.ts` — check: curl returns application/pdf; 403 for another user's invoice. ⚠️ risky: permission check.
3. Add "Download PDF" button to `InvoicePage.tsx` — check: clicking it in the dev server downloads the file.

## Out of scope
- Email delivery, bulk export.
```

## Rules

- Small steps beat big ones. If a step's check could fail for five different reasons, split it.
- Every step has a check. "Looks good" is not a check.
- Always write an "Out of scope" section. It stops scope creep.
- The plan should be readable in one minute: under ~600 words and ~12 steps. A longer plan is usually two plans.

## Files in this skill

- `templates/`: feature, bugfix, refactor and migration plans.
- [reference/risky-steps.md](reference/risky-steps.md): which steps to mark ⚠️, and safer ways to do them.
- [reference/good-questions.md](reference/good-questions.md): what to ask, what to decide yourself, and how to word it.
- [scripts/check_plan.py](scripts/check_plan.py): plan linter (Python 3.8+, no dependencies).
