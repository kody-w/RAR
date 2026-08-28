---
name: "rar-cowork-cookbook-scheduled-brief-track-supplier-managed-and-consignment-inventory"
description: "Schedulable morning-brief email summarizing track supplier managed and consignment inventory for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_track_supplier_managed_and_consignment_inventory", "rar_sha256": "c77ad0442379dff09f42b48d04884b7b7070f6bd068b02e939cb543dea628f47", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_track_supplier_managed_and_consignment_inventory`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_track_supplier_managed_and_consignment_inventory_agent.py` and in the RCI capsule.

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

Track supplier managed and consignment inventory Scheduled Email Brief — Schedulable morning-brief email summarizing track supplier managed and consignment inventory for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-track-supplier-managed-and-consignment-inventory
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_track_supplier_managed_and_consignment_inventory_agent.py` and embedded as the fenced Python below (sha256 c77ad0442379dff0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_track_supplier_managed_and_consignment_inventory_agent.py` first:

```bash
python3 scheduled_brief_track_supplier_managed_and_consignment_inventory_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_track_supplier_managed_and_consignment_inventory_agent.py   # or on stdin
python3 scheduled_brief_track_supplier_managed_and_consignment_inventory_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Track supplier managed and consignment inventory Scheduled Email Brief — Schedulable morning-brief email summarizing track supplier managed and consignment inventory for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-track-supplier-managed-and-consignment-inventory
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_track_supplier_managed_and_consignment_inventory',
    "version": '2.0.1',
    "display_name": 'Track supplier managed and consignment inventory Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing track supplier managed and consignment inventory for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-track-supplier-managed-and-consignment-inventory',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-track-supplier-managed-and-consignment-inventory',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e0c066d50431d90a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/maintain-inventory-levels/track-supplier-managed-and-consignment-inventory'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/scheduled-brief-track-supplier-managed-and-consignment-inventory', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ScheduledBriefTrackSupplierManagedAndConsignmentInventory(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefTrackSupplierManagedAndConsignmentInventory'
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
    print(ScheduledBriefTrackSupplierManagedAndConsignmentInventory().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
