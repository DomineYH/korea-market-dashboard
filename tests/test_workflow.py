import unittest
from pathlib import Path


class WorkflowTests(unittest.TestCase):
    def test_auto_update_workflow_runs_at_9_and_16_kst_and_commits_phase_outputs(self):
        workflow = Path(".github/workflows/auto-update.yml")
        self.assertTrue(workflow.exists())
        text = workflow.read_text(encoding="utf-8")
        self.assertIn("cron: '0 0 * * 1-5'", text)  # 09:00 KST prediction
        self.assertIn("cron: '0 7 * * 1-5'", text)  # 16:00 KST close analysis
        self.assertIn("phase", text)
        self.assertIn("--phase", text)
        self.assertIn("scripts/update.py", text)
        self.assertIn("DISCORD_WEBHOOK_URL", text)
        self.assertIn("reports/morning-prediction.md", text)
        self.assertIn("reports/close-analysis.md", text)
        self.assertIn("git push", text)


if __name__ == "__main__":
    unittest.main()
