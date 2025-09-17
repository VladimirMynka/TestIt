# Merge Request Protocol (ops.mr.v1)

<<AC_ANCHOR|PROTOCOL|OPS|mr@v1>>
This protocol standardizes how contributors prepare and submit merge requests.
It is role-neutral and focuses on coordination between architect, developer,
and tester sessions.
<</AC_ANCHOR|PROTOCOL|OPS|mr@v1>>

| Field | Details |
| --- | --- |
| **Goal** | Produce a reviewable MR aligned with contracts and roadmap commitments. |
| **Roles** | Architect (contracts/docs), Developer (implementation), Tester (verification). |
| **Preconditions** | Relevant roadmap item identified; contracts updated; metrics evaluated. |
| **Steps** | 1. Reconstruct context using SSOT. 2. Update roadmap/contracts if scope shifts. 3. Implement/tests per role. 4. Run mandated checks (`make lint test docs-check`). 5. Record metrics snapshot. 6. Compose MR summary referencing anchors. |
| **Artifacts** | Code/docs diffs, updated registries, metrics state file, MR description. |
| **Exit Criteria** | Clean git status, all checks passing, MR template completed. |
| **Rollback** | Revert commits; update roadmap with blockers. |
| **Incident Handling** | Escalate via SECURITY.md contacts (pending). |
