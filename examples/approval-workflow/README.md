# Human-approved workflow — runnable learning example

This minimal **standalone Python demonstration** illustrates a state machine for sensitive actions with explicit human approval. It is **not** a deployed Alyntara component and does not prove that the Digital Twin integrates with a backend.

## Run locally

Requires Python 3.10+; no third-party dependencies:

```bash
python -m unittest discover -s examples/approval-workflow -p 'test_*.py' -v
```

The example covers approval, rejection, bypass prevention, reviewer validation and duplicate-decision protection.

## Product relevance

This demonstrates why approval needs to be a **server-enforced state transition**, rather than a conversational instruction alone. In a real product it would also require authenticated reviewer identity, tenant isolation, an ACID-backed durable store, concurrency control, idempotent execution, audit logs, token security and integration tests.

## Honest scope

- In-memory state only, not a persisted backend.
- No production authentication, external actions, LLMs, live providers or Supabase dependency.
- Passing unit tests establish only this small state-machine behaviour.

[Portfolio](../../README.md) · [Digital Twin case study](../../projects/alyntara-digital-twin.md)
