# Sources of Truth Index

<<AC_ANCHOR|DOC|SOT|index@v1>>
This index maps conceptual domains to their authoritative documents or future
locations. When multiple artifacts reference the same knowledge, this table
identifies the canonical source. Information might lag behind implementation;
always confirm by inspecting the referenced files directly.
<</AC_ANCHOR|DOC|SOT|index@v1>>

| Domain | Primary SSOT | Notes |
| --- | --- | --- |
| Contracts & Interfaces | `/contracts/registry.yaml` | Enumerates active contract files and versions. |
| Protocols | `/protocols/registry.yaml` | Lists operational processes and their anchors. |
| Metrics & States | `/metrics/registry.yaml` | Defines tracked health metrics; live values in `/metrics/states`. |
| Triggers | `/triggers/registry.yaml` | Maps context patterns to required responses. |
| Roadmaps | `ROADMAP.md`, `/docs/roadmap/` | Strategic planning; see anchors for detail. |
| Anchors | `/docs/meta/anchors.md` | Stabilized anchor catalog. |
| Architecture Decisions | `/docs/decisions/adr-0001-llm-integration.md` | First accepted ADR governing LLM integration. |
| Project Health Summary (RU) | `/docs/meta/status_ru.md` | Человекоориентированный обзор; сверяйте с SSOT перед действиями. |
| Operational Tooling | `/ops/ci/`, `/ops/docker/`, `Makefile` | CI/CD and runtime scaffolding (currently placeholders). |
