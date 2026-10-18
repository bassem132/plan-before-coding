# Spotting risky steps

Mark a step ⚠️ when getting it wrong is expensive, hard to undo, or invisible until production. Do risky steps early, behind a check, or with explicit approval.

## Always risky

| Area | Why | Safer approach |
| --- | --- | --- |
| Database migrations, data backfills | Can destroy or corrupt data; slow on big tables | Dry run on a copy; reversible migration; compare row counts |
| Auth, permissions, sessions | Mistakes leak data or lock users out | Test as an unauthorized user too, not only the happy path |
| Payments, invoices, money math | Real money, legal records | Integer minor units (piasters/cents); provider test mode; exact-value tests |
| Public APIs, webhooks, URLs | Other systems depend on them | Keep the old shape working; version or deprecate |
| Deleting files, data or branches | Often irreversible | Ask first; move or archive instead of deleting |
| Config, env vars, secrets | Breaks every environment at once | Change one environment first; never commit secrets |
| Dependency upgrades (major versions) | Hidden breaking changes | Read the changelog; upgrade alone in its own step |
| Concurrency, caching, queues | Bugs appear only under load or timing | Write a test that forces the race; check cache invalidation |
| Time zones, dates, locales, RTL | Correct in one locale, wrong in another | Test with Africa/Cairo and UTC; test Arabic/RTL text |

## Signs a step is riskier than it looks

- You can't write its check yet.
- It touches code with no tests.
- It changes something that runs on a schedule, on deploy, or in another service.
- The words "just", "quickly" or "simply" appear in its description.
