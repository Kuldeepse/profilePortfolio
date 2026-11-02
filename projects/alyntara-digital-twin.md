# Alyntara Digital Twin — Durable Agent Workflow Case Study

**Product:** Human-controlled, API-integrated workflow system. **Stage:** Prototype and implementation exploration, with end-to-end acceptance outstanding.

## User problem
Many useful assistant tasks need multiple steps, external application permissions, interruptions, and approval before completion. A reliable workflow needs inspectable state rather than a single transient LLM response.

## Architecture and product choices
| Capability | Intended role | Why it matters |
| --- | --- | --- |
| Task and lifecycle model | Track work from intake through completion or failure | Visibility and recovery |
| Adapter registry | Isolate Gmail, Calendar and future providers | Safer integration changes |
| Durable state | Persist workflow and task progress | Resume and audit |
| Approval state | Require explicit human decision for sensitive steps | Accountability |
| Audit records | Record decisions and actions | Traceability and troubleshooting |
| Agent API boundary | Connect with Alyntara AI Agent | Independent release and interface contracts |

## Reported implementation history
Development discussions previously described task lifecycle models, adapter registry, runtime state/persistence, approval state and focused regression tests on isolated branches. A proposed Gmail-to-Calendar demonstration involved ingestion, summarisation, draft generation, availability checking, booking requests and human approval.

**Important:** These were development and review reports; the connected repository's default-branch README still states that it initially held planning material only. The reports are **not independently confirmed as a merged, deployed or working end-to-end release**.

## Unresolved gates
- Functional Google OAuth and scoped connector permissions.
- Live Gmail and Calendar workflow using authorised test accounts.
- Human approval and denial cases; repeat/retry idempotency.
- Exact-source regression testing, access control and audit verification.
- Reachable reviewer demonstration and production readiness.

## Evaluation hypothesis
A useful release should demonstrate a single task that persists through multiple steps and interruptions, requires approval before an external action, then records an auditable outcome. Measure completion, recovery, latency, approval correctness and failure paths before broadening capabilities.

[Private repository](https://github.com/Alyntara/Alyntara-Digital-Twin) · [Architecture](../architecture/README.md) · [Evidence register](../test-evidence) · [Portfolio](../README.md)
