---
name: "rar-cowork-cookbook-scheduled-brief-track-supplier-managed-and-consignment-inventory"
description: "Schedulable morning-brief email summarizing track supplier managed and consignment inventory for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_track_supplier_managed_and_consignment_inventory", "rar_sha256": "a0e6c566c8b684dac41327728b05c52025ad7059f0e01169722e614533d1ef32", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_track_supplier_managed_and_consignment_inventory_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-track-supplier-managed-and-consignment-inventory:0842d3538342b175879c90bda6ae4cbaa600fee7c4bd96a86bd5b221d3e2552f", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_track_supplier_managed_and_consignment_inventory`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_track_supplier_managed_and_consignment_inventory_agent.py` is
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
