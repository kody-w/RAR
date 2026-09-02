---
name: "rar-cowork-cookbook-demo-data-define-warehouse-management-kpis"
description: "Generates and creates realistic demo records for define warehouse management KPIs in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_define_warehouse_management_kpis", "rar_sha256": "40f92976de71c64532e7986881a9dd7fb163573a5e09e7919870eaca93783f66", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_define_warehouse_management_kpis_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-define-warehouse-management-kpis:1e78ac648ddf931c7e3cd575dd521e79f723beb325b8970311415ae6f3fe962b", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_define_warehouse_management_kpis`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_define_warehouse_management_kpis_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

Define warehouse management KPIs Demo Data Generator — Generates and creates realistic demo records for define warehouse management KPIs in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-define-warehouse-management-kpis
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "operation": {
      "description": "What to do: run, plan, checklist, describe.",
      "enum": [
        "run",
        "plan",
        "checklist",
        "describe"
      ],
      "type": "string"
    },
    "subject": {
      "description": "The process to automate.",
      "type": "string"
    },
    "trigger": {
      "description": "Optional. What starts it \u2014 schedule, event or manual.",
      "type": "string"
    }
  },
  "required": [
    "operation"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_define_warehouse_management_kpis_agent.py` and embedded as the fenced Python below (sha256 40f92976de71c645…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_define_warehouse_management_kpis_agent.py` first:

```bash
python3 demo_data_define_warehouse_management_kpis_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_define_warehouse_management_kpis_agent.py   # or on stdin
python3 demo_data_define_warehouse_management_kpis_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define warehouse management KPIs Demo Data Generator — Generates and creates realistic demo records for define warehouse management KPIs in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-define-warehouse-management-kpis
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_define_warehouse_management_kpis',
    "version": '2.0.0',
    "display_name": 'Define warehouse management KPIs Demo Data Generator',
    "description": 'Generates and creates realistic demo records for define warehouse management KPIs in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'community',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'demo-data-define-warehouse-management-kpis',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-define-warehouse-management-kpis',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2b23dc28f460b8b8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/analyze-warehouse-operations/define-warehouse-management-kpis'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/demo-data-define-warehouse-management-kpis', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Microsoft 365 Copilot Cowork'],
}


try:
    from agents.basic_agent import BasicAgent
except ModuleNotFoundError:
    class BasicAgent:
        def __init__(self, name, metadata):
            self.name = name
            self.metadata = metadata


# The toasted capability. The upstream entry supplies the WHAT; this procedure
# is RAR's own method for that shape of work, generated by
# @kody-w/skill_toaster_agent from the metadata we hold. No upstream text is
# reproduced here — see the module docstring.
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DemoDataDefineWarehouseManagementKpis(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataDefineWarehouseManagementKpis'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'The process to automate.', 'type': 'string'}, 'trigger': {'description': 'Optional. What starts it — schedule, event or manual.', 'type': 'string'}},
                "required": ["operation"],
            },
        }
        super().__init__(self.name, self.metadata)

    # ── helpers ─────────────────────────────────────────────────────────

    def _subject(self, kwargs):
        for key in ("subject", "input", "target", "topic"):
            value = str(kwargs.get(key) or "").strip()
            if value:
                return value
        return ""

    def _header(self, subject):
        label = subject or f"<no {_SPEC['subject_label']} supplied>"
        return f"{_SPEC['verb']}: {label}"

    def _context(self, kwargs):
        extras = []
        for key in _SPEC["params"]:
            if key == "subject":
                continue
            value = str(kwargs.get(key) or "").strip()
            if value:
                extras.append(f"{key}: {value}")
        return extras

    def _plan(self, subject, kwargs):
        lines = [self._header(subject)]
        extras = self._context(kwargs)
        if extras:
            lines += ["", "Context:"] + [f"  {e}" for e in extras]
        lines += ["", "Procedure:"]
        lines += [f"  {i}. {step}" for i, step in enumerate(_SPEC["steps"], 1)]
        if not subject:
            lines += [
                "",
                f"Pass subject=\u0022...\u0022 to bind this procedure to a "
                f"specific {_SPEC['subject_label']}.",
            ]
        return lines

    def _checklist(self):
        return ["Acceptance checks:"] + [f"  [ ] {c}" for c in _SPEC["checks"]]

    def _provenance(self):
        src = __manifest__["source"]
        lines = [
            f"{__manifest__['display_name']} (v{__manifest__['version']})",
            "",
            __manifest__["description"],
            "",
            f"Capability shape: {_SPEC['archetype']} "
            f"(confidence {_SPEC['confidence']})",
        ]
        platforms = __manifest__.get("platforms") or []
        if platforms:
            lines.append("Runs on:          " + ", ".join(platforms))
        lines += [
            "",
            f"Indexed from:     {src['source_name']}",
            f"Upstream entry:   {src['upstream_url']}",
            f"Upstream author:  {__manifest__['author']}",
            "",
            "RAR indexes this capability and implements its method; the "
            "upstream library remains the authority for its own instructions. "
            "Open the link above to get those from the source.",
        ]
        return lines

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

        if op == "describe":
            return "\n".join(self._provenance())

        if op == "checklist":
            return "\n".join([self._header(subject), ""] + self._checklist())

        if op == "plan":
            return "\n".join(self._plan(subject, kwargs))

        if op == "run":
            lines = self._plan(subject, kwargs)
            lines += [""] + self._checklist()
            lines += ["", f"Deliverable: {_SPEC['deliverable']}"]
            lines += ["", f"Source: {__manifest__['source']['upstream_url']}"]
            return "\n".join(lines)

        return (
            f"Unknown operation {op!r}. Valid operations: "
            + ", ".join(_SPEC["operations"])
        )


if __name__ == "__main__":
    print(DemoDataDefineWarehouseManagementKpis().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
