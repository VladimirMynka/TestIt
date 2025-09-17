# Release Protocol (ops.release.v1)

<<AC_ANCHOR|PROTOCOL|OPS|release@v1>>
Defines the coordinated steps for cutting a production release of the
conversational platform.
<</AC_ANCHOR|PROTOCOL|OPS|release@v1>>

| Field | Details |
| --- | --- |
| **Goal** | Deliver a tagged release artifact across core, plugins, and infrastructure. |
| **Roles** | Release manager, Core owner, Plugin owners, QA lead. |
| **Preconditions** | All MR protocols completed; CI green; release checklist acknowledged. |
| **Steps** | 1. Freeze merge queue. 2. Confirm contract versions and compatibility risk. 3. Trigger release pipeline (`make release` — pending). 4. Publish Docker images and version tags. 5. Update CHANGELOG and roadmap. 6. Announce via communication channels. |
| **Artifacts** | Release notes, tags, container images, updated metrics snapshot. |
| **Exit Criteria** | Deployment verified in staging/production with monitoring enabled. |
| **Rollback** | Execute `/protocols/migration.md` rollback section; redeploy previous tag. |
| **Incident Handling** | Engage incident response per SECURITY.md (pending). |
