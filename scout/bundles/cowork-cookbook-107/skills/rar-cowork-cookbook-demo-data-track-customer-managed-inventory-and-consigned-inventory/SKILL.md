---
name: "rar-cowork-cookbook-demo-data-track-customer-managed-inventory-and-consigned-inventory"
description: "Generates and creates realistic demo records for track customer managed inventory and consigned inventory in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_track_customer_managed_inventory_and_consigned_inventory", "rar_sha256": "98d8b7b128e14a39e7fe75b50b3ec6bf408e1c528b269cf262bbf13271384f1c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_track_customer_managed_inventory_and_consigned_inventory_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-track-customer-managed-inventory-and-consigned-inventory:5e0d950f1161b58105e411cbeef8a23faf951770d6be863813ac6a70ff6f7cd2", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_track_customer_managed_inventory_and_consigned_inventory`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_track_customer_managed_inventory_and_consigned_inventory_agent.py` is
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

Track customer managed inventory and consigned inventory Demo Data Generator — Generates and creates realistic demo records for track customer managed inventory and consigned inventory in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-track-customer-managed-inventory-and-consigned-inventory
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_track_customer_managed_inventory_and_consigned_inventory_agent.py` and embedded as the fenced Python below (sha256 98d8b7b128e14a39…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_track_customer_managed_inventory_and_consigned_inventory_agent.py` first:

```bash
python3 demo_data_track_customer_managed_inventory_and_consigned_inventory_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_track_customer_managed_inventory_and_consigned_inventory_agent.py   # or on stdin
python3 demo_data_track_customer_managed_inventory_and_consigned_inventory_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Track customer managed inventory and consigned inventory Demo Data Generator — Generates and creates realistic demo records for track customer managed inventory and consigned inventory in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-track-customer-managed-inventory-and-consigned-inventory
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_track_customer_managed_inventory_and_consigned_inventory',
    "version": '2.0.0',
    "display_name": 'Track customer managed inventory and consigned inventory Demo Data Generator',
    "description": 'Generates and creates realistic demo records for track customer managed inventory and consigned inventory in a sandbox tenant for training and pilot scenarios.',
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
        "upstream_slug": 'demo-data-track-customer-managed-inventory-and-consigned-inventory',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-track-customer-managed-inventory-and-consigned-inventory',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '37c9688d71c299cc',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/maintain-inventory-levels/track-customer-managed-inventory-and-consigned-inventory'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/demo-data-track-customer-managed-inventory-and-consigned-inventory', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DemoDataTrackCustomerManagedInventoryAndConsignedInventory(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataTrackCustomerManagedInventoryAndConsignedInventory'
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
    print(DemoDataTrackCustomerManagedInventoryAndConsignedInventory().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
