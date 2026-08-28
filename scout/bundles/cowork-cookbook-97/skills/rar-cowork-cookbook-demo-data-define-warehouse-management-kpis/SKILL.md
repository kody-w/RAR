---
name: "rar-cowork-cookbook-demo-data-define-warehouse-management-kpis"
description: "Generates and creates realistic demo records for define warehouse management KPIs in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_define_warehouse_management_kpis", "rar_sha256": "40f92976de71c64532e7986881a9dd7fb163573a5e09e7919870eaca93783f66", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_define_warehouse_management_kpis`. The original RAPP
agent is preserved byte-for-byte in `demo_data_define_warehouse_management_kpis_agent.py` and in the RCI capsule.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the linked
agent SHA-256 before importing it. If preflight reports a host dependency that
Scout cannot satisfy, use the `brainstem_chat` MCP tool to run the canonical
agent in the user's Brainstem. Never paraphrase the factory or agent into a new
implementation. The generic direct-file commands in the generated Toaster
section are recovery guidance; Scout should prefer the verified runner.

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
