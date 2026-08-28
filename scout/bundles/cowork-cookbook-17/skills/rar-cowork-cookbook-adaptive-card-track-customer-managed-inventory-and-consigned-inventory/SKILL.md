---
name: "rar-cowork-cookbook-adaptive-card-track-customer-managed-inventory-and-consigned-inventory"
description: "Produces a reusable Adaptive Card JSON snapshot of track customer managed inventory and consigned inventory status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_track_customer_managed_inventory_and_consigned_inventory", "rar_sha256": "0bef6f133be31988472a99107e703cdc25f8efd44b6ba807ad959c428162fe3e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_track_customer_managed_inventory_and_consigned_inventory_agent.py` and embedded as the fenced Python below (sha256 0bef6f133be31988…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_track_customer_managed_inventory_and_consigned_inventory_agent.py` first:

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
    "version": '2.0.0',
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
