"""Run: python -m unittest discover -s examples/approval-workflow -p 'test_*.py'."""
import unittest
from workflow import Task, Status


class WorkflowTests(unittest.TestCase):
    def test_happy_path(self):
        t = Task("Draft an appointment request")
        t.request_approval()
        t.decide("reviewer", approve=True)
        t.complete()
        self.assertEqual(t.status, Status.COMPLETED)
        self.assertEqual(t.approved_by, "reviewer")

    def test_rejection_blocks_execution(self):
        t = Task("Send an external message")
        t.request_approval()
        t.decide("reviewer", approve=False)
        with self.assertRaises(PermissionError):
            t.complete()
        self.assertEqual(t.status, Status.REJECTED)

    def test_cannot_bypass_review(self):
        t = Task("External action")
        with self.assertRaises(PermissionError):
            t.complete()

    def test_reviewer_required(self):
        t = Task("Action")
        t.request_approval()
        with self.assertRaises(ValueError):
            t.decide("", approve=True)

    def test_repeated_decisions_rejected(self):
        t = Task("Action")
        t.request_approval()
        t.decide("reviewer", approve=True)
        with self.assertRaises(ValueError):
            t.decide("another reviewer", approve=True)


if __name__ == "__main__":
    unittest.main()
