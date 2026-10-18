# Plan before coding

Makes your AI agent write a short plan of small, verifiable steps before touching code, so it builds the right thing the first time.

A portable agent skill (`SKILL.md`) that works in **Claude Code**, **Codex** and **Cursor**.

## Install

### Claude Code (plugin)

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

### Cursor

Copy the folder into your project's `.cursor/skills/`, or paste the body of `SKILL.md` into a rule in `.cursor/rules/plan-before-coding.mdc`.

## What's inside

```
skills/plan-before-coding/SKILL.md   the skill
```

See [skills/plan-before-coding/SKILL.md](skills/plan-before-coding/SKILL.md) for when it triggers and what it does.

## Author

Bassem Mo’men — [@bassem132](https://github.com/bassem132)

## License

MIT — see [LICENSE](LICENSE).
