# Plan before coding

Agents that start coding right away often build the wrong thing with confidence. This skill makes the agent read the code, write a short plan of small steps (each with a file and a check), flag the risky steps, and (for big or risky changes) wait for your go-ahead. Small, clear changes get a 3–5 line inline plan and the agent proceeds.

A portable agent skill (`SKILL.md` plus scripts and references) for **Claude Code**, **Codex** and **Cursor**. The scripts have no dependencies (Python 3.8+ / bash 3.2+).

## What's inside

| File | What it does |
| --- | --- |
| `skills/plan-before-coding/SKILL.md` | When it triggers and the procedure |
| `skills/plan-before-coding/templates/` | Feature, bug fix, refactor and migration plans |
| `skills/plan-before-coding/reference/risky-steps.md` | Which steps to mark ⚠️ (data, auth, money, APIs, RTL…) and safer approaches |
| `skills/plan-before-coding/reference/good-questions.md` | What to ask, what to decide yourself, and how to word it |
| `skills/plan-before-coding/scripts/check_plan.py` | Plan linter: every step has a file and a real check, sections present, size |
| `adapters/cursor/plan-before-coding.mdc` | Ready-made Cursor rule |
| `adapters/codex/AGENTS.snippet.md` | Short version to paste into any `AGENTS.md` |
| `evals/evals.json` | Test prompts: should it trigger, and what should the agent do |
| `tests/` | Unit tests for the scripts |

## Install

### Claude Code (plugin, recommended)

```
/plugin marketplace add bassem132/plan-before-coding
/plugin install plan-before-coding@plan-before-coding
```

### Claude Code (manual)

```bash
git clone https://github.com/bassem132/plan-before-coding.git
cp -r plan-before-coding/skills/plan-before-coding ~/.claude/skills/
```

### Codex

```bash
cp -r plan-before-coding/skills/plan-before-coding ~/.codex/skills/
```

Or paste `adapters/codex/AGENTS.snippet.md` into your `AGENTS.md`.

### Cursor

```bash
mkdir -p .cursor/rules .cursor/skills
cp plan-before-coding/adapters/cursor/plan-before-coding.mdc .cursor/rules/
cp -r plan-before-coding/skills/plan-before-coding .cursor/skills/      # so the agent can run the scripts
```

## Try the script

```bash
python3 skills/plan-before-coding/scripts/check_plan.py plan.md
```

## Develop

```bash
python3 -m unittest discover -s tests -v
claude plugin validate .
```

To check that the skill changes behaviour, run the prompts in `evals/evals.json` in a fresh session with the skill installed. Every `expect` item should hold, and prompts with `should_trigger: false` must not load the skill.

## Using with other skills

These four are meant to work as a set, and some overlap with popular skill packs.

| If you also have | Then |
| --- | --- |
| `verification-before-completion` | Keep `verify-before-done`; it adds the repo-aware command finder and the commit/PR gate. Disable the other to avoid double checks. |
| `systematic-debugging` / `diagnosing-bugs` | Pick one as the main loop. `debug-root-cause` adds `what_changed.sh`, a bug-patterns reference and a report format. |
| `writing-plans` | Pick one per task. `plan-before-coding` has a lightweight mode for small changes. |
| Built-in assistant memory | `learn-from-corrections` is for shared repo rules in `AGENTS.md`; keep personal preferences in memory, not both. |

## Author

Bassem Moumen · [@bassem132](https://github.com/bassem132)

## License

MIT, see [LICENSE](LICENSE).
