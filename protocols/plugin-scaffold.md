# Plugin Scaffold Protocol (ops.plugin-scaffold.v1)

<<AC_ANCHOR|PROTOCOL|OPS|plugin-scaffold@v1>>
Guides creation of a new plugin service compatible with the platform's
contracts and operational practices.
<</AC_ANCHOR|PROTOCOL|OPS|plugin-scaffold@v1>>

| Field | Details |
| --- | --- |
| **Goal** | Produce a plugin repository structure aligned with `plugin.contract.v1`. |
| **Roles** | Plugin architect, plugin developer, QA contact. |
| **Preconditions** | Approved plugin idea linked to roadmap; tag assigned; contract compatibility assessed. |
| **Steps** | 1. Copy `/plugins/_templates` into a new plugin folder. 2. Update contract references and schema files. 3. Register plugin via `/plugins/register` endpoint (mock). 4. Implement service logic following shared LLM client usage. 5. Add tests under `/tests/plugins`. 6. Update metrics and documentation. |
| **Artifacts** | Plugin descriptor, JSON Schemas, test plan, metrics snapshot. |
| **Exit Criteria** | Plugin passes contract tests; registry updated; MR merged. |
| **Rollback** | Remove plugin folder; update registries and roadmap to reflect status. |
| **Incident Handling** | Notify platform security if plugin exposes sensitive data. |
