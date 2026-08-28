---
name: "rar-cowork-cookbook-demo-data-define-warehouse-management-kpis"
description: "Generates and creates realistic demo records for define warehouse management KPIs in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_define_warehouse_management_kpis", "rar_sha256": "c3dced4408a23d5be0d41611c9b135af5c8e45a05fa9e6ced2a034d313eee4a1", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_define_warehouse_management_kpis_agent.py` and embedded as the fenced Python below (sha256 c3dced4408a23d5b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_define_warehouse_management_kpis_agent.py` first:

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
    "version": '2.0.1',
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
