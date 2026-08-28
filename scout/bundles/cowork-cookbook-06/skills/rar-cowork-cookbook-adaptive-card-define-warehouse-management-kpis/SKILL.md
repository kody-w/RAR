---
name: "rar-cowork-cookbook-adaptive-card-define-warehouse-management-kpis"
description: "Produces a reusable Adaptive Card JSON snapshot of define warehouse management KPIs status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_define_warehouse_management_kpis", "rar_sha256": "bf016df58bddb441a967ec9390958ada87c608b68e5c949328bff22d51bdc726", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_define_warehouse_management_kpis`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_define_warehouse_management_kpis_agent.py` and in the RCI capsule.

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

Define warehouse management KPIs Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of define warehouse management KPIs status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-define-warehouse-management-kpis
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_define_warehouse_management_kpis_agent.py` and embedded as the fenced Python below (sha256 bf016df58bddb441…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_define_warehouse_management_kpis_agent.py` first:

```bash
python3 adaptive_card_define_warehouse_management_kpis_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_define_warehouse_management_kpis_agent.py   # or on stdin
python3 adaptive_card_define_warehouse_management_kpis_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define warehouse management KPIs Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of define warehouse management KPIs status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-define-warehouse-management-kpis
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_define_warehouse_management_kpis',
    "version": '2.0.1',
    "display_name": 'Define warehouse management KPIs Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of define warehouse management KPIs status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-define-warehouse-management-kpis',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-define-warehouse-management-kpis',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd8d95805d858ecd7',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/analyze-warehouse-operations/define-warehouse-management-kpis'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/adaptive-card-define-warehouse-management-kpis', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class AdaptiveCardDefineWarehouseManagementKpis(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardDefineWarehouseManagementKpis'
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
    print(AdaptiveCardDefineWarehouseManagementKpis().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
