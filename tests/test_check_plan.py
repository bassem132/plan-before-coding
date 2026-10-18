import os, subprocess, sys, unittest, glob

HERE = os.path.dirname(os.path.abspath(__file__))
SKILL = os.path.join(HERE, "..", "skills", "plan-before-coding")
SCRIPT = os.path.join(SKILL, "scripts", "check_plan.py")

GOOD = """## Goal
Users can export invoices as PDF.

## Steps
1. Add `renderInvoicePdf` in `src/invoices/pdf.ts` — check: unit test renders a sample.
2. Add route in src/routes/invoices.ts — check: curl returns application/pdf. ⚠️ risky: permissions.

## Out of scope
- Bulk export.
"""


def run(text):
    out = subprocess.run([sys.executable, SCRIPT, "-"], input=text, capture_output=True, text=True)
    return out.returncode, out.stdout


class CheckPlanTests(unittest.TestCase):
    def test_good_plan_passes(self):
        code, out = run(GOOD)
        self.assertEqual(code, 0, out)
        self.assertIn("risky step marked", out)

    def test_step_without_check(self):
        code, out = run(GOOD.replace(" — check: unit test renders a sample.", ""))
        self.assertEqual(code, 1)
        self.assertIn("no 'check:'", out)

    def test_vague_check(self):
        code, out = run(GOOD.replace("check: unit test renders a sample.", "check: looks good"))
        self.assertIn("vague check", out)

    def test_step_without_file(self):
        code, out = run(GOOD.replace("in `src/invoices/pdf.ts`", "somewhere").replace("`renderInvoicePdf`", "a renderer"))
        self.assertIn("doesn't name a file", out)

    def test_missing_sections(self):
        code, out = run("## Steps\n1. Do `a.ts` — check: `make test`\n")
        self.assertIn("No 'Goal'", out)
        self.assertIn("No 'Out of scope'", out)

    def test_templates_have_placeholders(self):
        for path in glob.glob(os.path.join(SKILL, "templates", "*.md")):
            out = subprocess.run([sys.executable, SCRIPT, path], capture_output=True, text=True)
            self.assertEqual(out.returncode, 1, path)
            self.assertIn("Unfilled placeholders", out.stdout, path)

    def test_skill_example_passes(self):
        with open(os.path.join(SKILL, "SKILL.md"), encoding="utf-8") as fh:
            text = fh.read()
        example = text.split("```markdown\n", 1)[1].split("```", 1)[0]
        code, out = run(example)
        self.assertEqual(code, 0, out)


if __name__ == "__main__":
    unittest.main()
