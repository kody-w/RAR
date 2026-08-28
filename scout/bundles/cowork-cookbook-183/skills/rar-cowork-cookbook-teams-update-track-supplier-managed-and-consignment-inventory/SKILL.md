---
name: "rar-cowork-cookbook-teams-update-track-supplier-managed-and-consignment-inventory"
description: "Drafts a Teams channel post on track supplier managed and consignment inventory status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_track_supplier_managed_and_consignment_inventory", "rar_sha256": "79416024d8ecf63796dea1e75b82a2cb745ffb2604ecd1f2be8ea96e5ecc2344", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_track_supplier_managed_and_consignment_inventory`. The original RAPP
agent is preserved byte-for-byte in `teams_update_track_supplier_managed_and_consignment_inventory_agent.py` and in the RCI capsule.

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
