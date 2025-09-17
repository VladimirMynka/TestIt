# Migration Protocol (ops.migration.v1)

<<AC_ANCHOR|PROTOCOL|OPS|migration@v1>>
Describes the safe process for introducing schema and data migrations while
maintaining service availability.
<</AC_ANCHOR|PROTOCOL|OPS|migration@v1>>

| Field | Details |
| --- | --- |
| **Goal** | Plan, execute, and validate database or schema migrations without downtime. |
| **Roles** | Database owner, Core developer, QA representative, SRE. |
| **Preconditions** | Migration design reviewed; backups verified; feature flags ready. |
| **Steps** | 1. Document migration intent and impact in `/docs/decisions/`. 2. Create Alembic script under `/core/migrations`. 3. Dry-run using `make migrate` against staging. 4. Monitor metrics `core.db.migration.duration` and error logs. 5. Execute production migration during approved window. 6. Validate via smoke tests. |
| **Artifacts** | Migration script, rollout checklist, metrics snapshot, rollback plan. |
| **Exit Criteria** | Schema updated; services operational; monitoring steady. |
| **Rollback** | Use backups/point-in-time recovery; revert schema changes; document incident. |
| **Incident Handling** | Trigger incident response and notify stakeholders immediately. |
