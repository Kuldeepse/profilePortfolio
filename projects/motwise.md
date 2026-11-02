# MOTWise — Vehicle Service Product Case Study

**Product:** Digital MOT and vehicle-servicing customer journeys. **Stage:** Development and owner review.

## Product opportunity
Simplify discovery of MOT/servicing options, service selection, booking and follow-up while keeping pricing, payments and customer actions transparent.

## Product and engineering focus
- Responsive service discovery and booking journeys.
- Integration boundaries for providers and transactional services.
- Payment-provider abstraction, test-mode Stripe verification and explicit controls preventing premature real charges.
- Testable acceptance criteria for page flows, validation, errors and mobile usability.
- Preview deployments, release traceability and owner sign-off.

## Delivery history and release decisions
Project discussions refer to a controlled UI review branch, iterative review runs, and payment-verification changes. A prior successful CI validation for one revision does not prove that the latest intended interface is deployed or accepted.

## Risks and remaining acceptance
The live UI has previously been reported as not reflecting the intended release. Full responsive UI review, end-to-end service journeys, security checks and test-mode payment evidence remain to be demonstrated. **Production charging is not claimed enabled.**

## Metrics to validate
Task completion, booking funnel drop-off, payment failure handling, responsive UI defects, error recovery and customer support readiness. No fabricated outcomes are presented.

[Project website](https://motwiseai.duckdns.org/) · [Demonstration index](../screenshots/README.md) · [Test approach](../docs/testing-approach.md) · [Portfolio](../README.md)
