"""Small standalone example: human-approved workflow state machine.

Demonstrates state transitions only. No database, LLM, external API or production auth.
"""
from dataclasses import dataclass
from enum import Enum


class Status(str, Enum):
    NEW = "new"
    AWAITING_APPROVAL = "awaiting_approval"
    APPROVED = "approved"
    REJECTED = "rejected"
    COMPLETED = "completed"


@dataclass
class Task:
    title: str
    status: Status = Status.NEW
    approved_by: str | None = None

    def request_approval(self) -> None:
        if self.status != Status.NEW:
            raise ValueError("Approval can only be requested for a new task")
        self.status = Status.AWAITING_APPROVAL

    def decide(self, reviewer: str, approve: bool) -> None:
        if self.status != Status.AWAITING_APPROVAL:
            raise ValueError("Task is not awaiting approval")
        if not reviewer.strip():
            raise ValueError("Reviewer is required")
        self.approved_by = reviewer if approve else None
        self.status = Status.APPROVED if approve else Status.REJECTED

    def complete(self) -> None:
        if self.status != Status.APPROVED:
            raise PermissionError("Only approved tasks can be completed")
        self.status = Status.COMPLETED
