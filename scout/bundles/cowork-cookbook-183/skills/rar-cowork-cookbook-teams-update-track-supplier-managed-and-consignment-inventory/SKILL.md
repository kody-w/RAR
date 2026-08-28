---
name: "rar-cowork-cookbook-teams-update-track-supplier-managed-and-consignment-inventory"
description: "Drafts a Teams channel post on track supplier managed and consignment inventory status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_track_supplier_managed_and_consignment_inventory", "rar_sha256": "6cb1520c20f6ba519d05f4a9d7bfb9feb2d52eb0754ab6c6cf12ded8ae17e656", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_track_supplier_managed_and_consignment_inventory_agent.py` and embedded as the fenced Python below (sha256 6cb1520c20f6ba51…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_track_supplier_managed_and_consignment_inventory_agent.py` first:

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
    "version": '2.0.1',
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
