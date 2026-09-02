---
name: "rar-cowork-cookbook-adaptive-card-track-customer-managed-inventory-and-consigned-inventory"
description: "Produces a reusable Adaptive Card JSON snapshot of track customer managed inventory and consigned inventory status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_track_customer_managed_inventory_and_consigned_inventory", "rar_sha256": "0bef6f133be31988472a99107e703cdc25f8efd44b6ba807ad959c428162fe3e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_track_customer_managed_inventory_and_consigned_inventory_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-track-customer-managed-inventory-and-consigned-inventory:d2c9e51ca4a8def4d9b7303129fb54bb46b16be4db897f7c7f2197ad759b9387", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_track_customer_managed_inventory_and_consigned_inventory`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_track_customer_managed_inventory_and_consigned_inventory_agent.py` is
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
