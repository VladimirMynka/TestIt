# Roadmap Skeleton

<<AC_ANCHOR|ROADMAP|GLOBAL|baseline@v1>>
This roadmap captures the long-term intent and immediate bootstrap activities
for the conversational platform. Information herein complements the SSOT
entries and may lag behind; verify against contract and protocol registries.
<</AC_ANCHOR|ROADMAP|GLOBAL|baseline@v1>>

## Vision (Long-Term)
1. Deliver a modular FastAPI-based core with plugin orchestration.
2. Ensure every interface is governed by explicit contracts and shared tests.
3. Provide cross-channel clients starting with Telegram and expanding via the
   shared API surface.

## Current Bootstrap Sprint
- **Goal:** Establish documentation, contract, and protocol frameworks without
  adding executable code.
- **Deliverables:** Repository skeleton, registry files, base metrics snapshot,
  and foundational architecture decisions recorded as ADRs.
- **Exit Criteria:** All mandatory scaffolding artifacts committed; metrics
  logged in `/metrics/states`; at least one ADR accepted to guide development.

## Recent Updates
- 2025-09-17: Accepted LLM integration strategy ADR
  (`/docs/decisions/adr-0001-llm-integration.md`).

## Backlog (High-Level)
- [x] Draft architecture decision record for LLM provider integration (see
  `<<AC_ANCHOR|DOC|DECISION|adr-llm-integration@v1>>`).
- [ ] Prepare developer onboarding documentation in `/docs/runbooks` aligned
  with protocols.
- [ ] Define CI/CD pipelines for linting, testing, and security scans; replace
  placeholder Makefile/CI commands with real implementations.

## Dependencies & Assumptions
- Contracts remain the SSOT for service interfaces; ADRs must reference their
  anchors to prevent drift.
- CI/security work requires stakeholder approval on tooling choices captured in
  future ADRs.
