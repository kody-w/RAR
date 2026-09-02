---
name: "rar-cowork-cookbook-teams-update-track-supplier-managed-and-consignment-inventory"
description: "Drafts a Teams channel post on track supplier managed and consignment inventory status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_track_supplier_managed_and_consignment_inventory", "rar_sha256": "79416024d8ecf63796dea1e75b82a2cb745ffb2604ecd1f2be8ea96e5ecc2344", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_track_supplier_managed_and_consignment_inventory_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-track-supplier-managed-and-consignment-inventory:7e6bcfe717b90f965e1c8fc6b43740a46c02d048d43f76c0356da03c6c56c254", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_track_supplier_managed_and_consignment_inventory`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_track_supplier_managed_and_consignment_inventory_agent.py` is
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

Track supplier managed and consignment inventory Teams Channel Update — Drafts a Teams channel post on track supplier managed and consignment inventory status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-track-supplier-managed-and-consignment-inventory
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_track_supplier_managed_and_consignment_inventory_agent.py` and embedded as the fenced Python below (sha256 79416024d8ecf637…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_track_supplier_managed_and_consignment_inventory_agent.py` first:

```bash
python3 teams_update_track_supplier_managed_and_consignment_inventory_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_track_supplier_managed_and_consignment_inventory_agent.py   # or on stdin
python3 teams_update_track_supplier_managed_and_consignment_inventory_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Track supplier managed and consignment inventory Teams Channel Update — Drafts a Teams channel post on track supplier managed and consignment inventory status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-track-supplier-managed-and-consignment-inventory
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_track_supplier_managed_and_consignment_inventory',
    "version": '2.0.0',
    "display_name": 'Track supplier managed and consignment inventory Teams Channel Update',
    "description": 'Drafts a Teams channel post on track supplier managed and consignment inventory status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-track-supplier-managed-and-consignment-inventory',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-track-supplier-managed-and-consignment-inventory',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b0a5b67e07845ae0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/maintain-inventory-levels/track-supplier-managed-and-consignment-inventory'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/teams-update-track-supplier-managed-and-consignment-inventory', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateTrackSupplierManagedAndConsignmentInventory(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateTrackSupplierManagedAndConsignmentInventory'
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
    print(TeamsUpdateTrackSupplierManagedAndConsignmentInventory().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
