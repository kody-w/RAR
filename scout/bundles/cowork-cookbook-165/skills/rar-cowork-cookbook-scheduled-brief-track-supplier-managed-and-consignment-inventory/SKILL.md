---
name: "rar-cowork-cookbook-scheduled-brief-track-supplier-managed-and-consignment-inventory"
description: "Schedulable morning-brief email summarizing track supplier managed and consignment inventory for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_track_supplier_managed_and_consignment_inventory", "rar_sha256": "a0e6c566c8b684dac41327728b05c52025ad7059f0e01169722e614533d1ef32", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_track_supplier_managed_and_consignment_inventory_agent.py` and embedded as the fenced Python below (sha256 a0e6c566c8b684da…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_track_supplier_managed_and_consignment_inventory_agent.py` first:

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
    "version": '2.0.0',
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
