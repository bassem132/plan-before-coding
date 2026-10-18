# Questions worth asking before coding

Ask only the questions whose answer changes the plan, three at most. For everything else, choose the conventional default and list it under Assumptions so the user can correct it.

## Worth asking

- **Who uses it, and where?** "Admins only, or every user?" changes auth, UI and tests.
- **What does done look like?** "Should the export include line items, or only totals?"
- **Which existing thing should this match?** "Should it look and behave like the Orders export?"
- **What must not change?** "Is anything else calling this endpoint?"
- **How much data or traffic?** "Tens of rows or millions?" changes the approach.
- **Is it reversible?** For deletes, migrations and sends: "Can we test on a copy first?"

## Not worth asking. Decide and note it as an assumption.

- Variable names, file names, folder layout when a pattern already exists.
- Which library, when the repo already uses one for this job.
- Formatting and style, which the linter and existing code answer.
- Anything you can find out by reading the code for two minutes.

## Phrasing

Offer a default with each question so a one-word answer works:

> Should the PDF include line items? I'll include them unless you say otherwise.
