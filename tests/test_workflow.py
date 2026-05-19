import unittest
from pathlib import Path


class WorkflowTests(unittest.TestCase):
    def test_auto_update_workflow_runs_after_korea_market_close_and_commits_outputs(self):
        workflow = Path(".github/workflows/auto-update.yml")
        self.assertTrue(workflow.exists())
        text = workflow.read_text(encoding="utf-8")
        self.assertIn("cron: '0 7 * * 1-5'", text)  # 16:00 KST, after 15:30 close
        self.assertIn("scripts/update.py", text)
        self.assertIn("DISCORD_WEBHOOK_URL", text)
        self.assertIn("git push", text)


if __name__ == "__main__":
    unittest.main()
