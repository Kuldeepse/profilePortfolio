# Product & AI Testing Approach

**Evidence classification:** This is a release evaluation framework, not a certificate of passing tests.

## Test layers

| Layer | Example scenarios | Acceptance evidence |
| --- | --- | --- |
| Functional | Core task flow, errors, cancellation and retries | Reproducible run and assertions |
| API/integration | Authentication, scopes, timeouts, idempotency | Test logs, synthetic fixtures, API contract |
| LLM quality | Grounding, task success, refusal, tool selection | Labelled dataset, scoring rubric, error analysis |
| Voice | Multilingual STT, latency, interruptions, stop command | Recorded consented/synthetic samples and result counts |
| Workflow | Restart recovery, persistence, approval denial | State snapshots, event trace and audit checks |
| Security | Permission isolation, secrets, dependency review | Reviewed findings and remediation evidence |
| UX/accessibility | Keyboard/mobile flows, task completion | Device matrix and owner acceptance |
| Release | Exact-source build, CI, deployment and rollback | Full SHA, CI URL, verified deployment URL |

## What every reported run must contain

- Full source commit SHA and branch
- Test execution date/time and environment
- Exact test command, dataset and expected result
- Passed, failed, blocked and skipped counts
- Links to the CI run or sanitised evidence
- Defects, limitations, reviewer and release decision

## Current evidence limitations

During this portfolio update, the default-branch READMEs in the connected private Alyntara repositories were inspected. The AI Agent README describes an initial baseline without imported application source; the Digital Twin README describes planning workstreams. These READMEs **do not confirm** that previous development/test progress was merged or verified on default branches.

No claim of complete end-to-end passing tests, operational production deployment, or measured model-quality benchmarks is made here.

[Project portfolio](../README.md) · [Current evidence register](../test-evidence)
