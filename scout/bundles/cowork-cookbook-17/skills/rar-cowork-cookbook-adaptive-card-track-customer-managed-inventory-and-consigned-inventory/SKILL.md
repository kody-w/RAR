---
name: "rar-cowork-cookbook-adaptive-card-track-customer-managed-inventory-and-consigned-inventory"
description: "Produces a reusable Adaptive Card JSON snapshot of track customer managed inventory and consigned inventory status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_track_customer_managed_inventory_and_consigned_inventory", "rar_sha256": "7b726084b6fb4187e9c063031ffaa932782342429c2afee2540bc0bf84fc3c1b", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_track_customer_managed_inventory_and_consigned_inventory`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_track_customer_managed_inventory_and_consigned_inventory_agent.py` and in the RCI capsule.

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

Track customer managed inventory and consigned inventory Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of track customer managed inventory and consigned inventory status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-track-customer-managed-inventory-and-consigned-inventory
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_track_customer_managed_inventory_and_consigned_inventory_agent.py` and embedded as the fenced Python below (sha256 7b726084b6fb4187…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_track_customer_managed_inventory_and_consigned_inventory_agent.py` first:

```bash
python3 adaptive_card_track_customer_managed_inventory_and_consigned_inventory_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_track_customer_managed_inventory_and_consigned_inventory_agent.py   # or on stdin
python3 adaptive_card_track_customer_managed_inventory_and_consigned_inventory_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Track customer managed inventory and consigned inventory Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of track customer managed inventory and consigned inventory status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-track-customer-managed-inventory-and-consigned-inventory
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_track_customer_managed_inventory_and_consigned_inventory',
    "version": '2.0.1',
    "display_name": 'Track customer managed inventory and consigned inventory Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of track customer managed inventory and consigned inventory status for embedding in dashboards, emails, or Teams.',
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
        "upstream_slug": 'adaptive-card-track-customer-managed-inventory-and-consigned-inventory',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-track-customer-managed-inventory-and-consigned-inventory',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ab2135e4fb5fb867',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/maintain-inventory-levels/track-customer-managed-inventory-and-consigned-inventory'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/adaptive-card-track-customer-managed-inventory-and-consigned-inventory', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class AdaptiveCardTrackCustomerManagedInventoryAndConsignedInventory(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardTrackCustomerManagedInventoryAndConsignedInventory'
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
    print(AdaptiveCardTrackCustomerManagedInventoryAndConsignedInventory().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
