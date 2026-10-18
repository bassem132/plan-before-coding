#!/usr/bin/env python3
"""Check that a written plan follows the plan-before-coding format.

Checks: a Goal section, numbered steps, a check on every step, files named
in every step, an Out of scope section, no unfilled <placeholders>, and a plan
short enough to read in about a minute.

Usage:
    python3 check_plan.py PLAN.md
    python3 check_plan.py -          # read the plan from stdin

Exit code: 0 = plan OK, 1 = problems found, 2 = file not found.
Works on Python 3.8+ with no dependencies.
"""
import re
import sys

MAX_WORDS = 600
MAX_STEPS = 12


def check(text):
    problems = []
    lower = text.lower()
    lines = text.splitlines()

    if not re.search(r"^#{1,6}\s*(goal|symptom|why)\b", text, re.I | re.M):
        problems.append("No 'Goal' section (or 'Symptom'/'Why' for bug fixes and refactors).")
    if not re.search(r"^#{1,6}\s*out of scope\b", text, re.I | re.M):
        problems.append("No 'Out of scope' section. Write it down, even if it's '- Nothing'.")

    steps = []
    in_steps = False
    for i, line in enumerate(lines, 1):
        if re.match(r"^#{1,6}\s*steps\b", line, re.I):
            in_steps = True
            continue
        if in_steps and re.match(r"^#{1,6}\s", line):
            in_steps = False
        if in_steps:
            m = re.match(r"^\s*(\d+)[.)]\s+(.*)", line)
            if m:
                steps.append((i, m.group(1), m.group(2)))

    if not steps:
        problems.append("No numbered steps under a 'Steps' heading.")
    if len(steps) > MAX_STEPS:
        problems.append("%d steps. Plans over %d steps usually hide a second plan; split it." % (len(steps), MAX_STEPS))

    for line_no, num, body in steps:
        if not re.search(r"\bcheck\s*:", body, re.I):
            problems.append("Step %s (line %d) has no 'check:'. Every step needs a test, command or visible result."
                            % (num, line_no))
        elif re.search(r"check\s*:\s*(looks? (good|fine|ok)|works|done|verify( it)?)\s*\.?$", body, re.I):
            problems.append("Step %s (line %d) has a vague check. Name the test, command or what you'll see."
                            % (num, line_no))
        if not re.search(r"`[^`]+`|\b[\w-]+/[\w./-]+|\b[\w-]+\.(?:[a-z]{1,5})\b", body):
            problems.append("Step %s (line %d) doesn't name a file. Say where the change happens." % (num, line_no))

    placeholders = re.findall(r"<[a-z][^<>\n]{2,80}>", text)
    placeholders = [p for p in placeholders if not re.match(r"<(br|/?[a-z]+)>$", p)]
    if placeholders:
        problems.append("Unfilled placeholders: %s" % ", ".join(sorted(set(placeholders))[:5]))

    words = len(re.findall(r"\w+", text))
    if words > MAX_WORDS:
        problems.append("Plan is %d words. Keep it under ~%d so it can be read in a minute." % (words, MAX_WORDS))

    risky = "⚠" in text or "risky" in lower
    return problems, len(steps), risky


def main(argv):
    if not argv:
        print(__doc__.strip(), file=sys.stderr)
        return 2
    path = argv[0]
    try:
        text = sys.stdin.read() if path == "-" else open(path, encoding="utf-8").read()
    except OSError as err:
        print("Can't read %s: %s" % (path, err), file=sys.stderr)
        return 2
    problems, n_steps, risky = check(text)
    print("%d steps%s" % (n_steps, ", risky step marked" if risky else ", no risky step marked"))
    if not problems:
        print("Plan OK.")
        return 0
    for p in problems:
        print("  - " + p)
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
