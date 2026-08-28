---
name: "rar-cowork-cookbook-adaptive-card-manage-service-truck-inventory"
description: "Produces a reusable Adaptive Card JSON snapshot of manage service truck inventory status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_manage_service_truck_inventory", "rar_sha256": "aad920d5de80ad785380d679c6db5e554303de13c1c918e38e0b2da1a6089235", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_manage_service_truck_inventory`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_manage_service_truck_inventory_agent.py` and in the RCI capsule.

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

Manage service truck inventory Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of manage service truck inventory status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-manage-service-truck-inventory
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_manage_service_truck_inventory_agent.py` and embedded as the fenced Python below (sha256 aad920d5de80ad78…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_manage_service_truck_inventory_agent.py` first:

```bash
python3 adaptive_card_manage_service_truck_inventory_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_manage_service_truck_inventory_agent.py   # or on stdin
python3 adaptive_card_manage_service_truck_inventory_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage service truck inventory Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of manage service truck inventory status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-manage-service-truck-inventory
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_manage_service_truck_inventory',
    "version": '2.0.1',
    "display_name": 'Manage service truck inventory Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of manage service truck inventory status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-manage-service-truck-inventory',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-manage-service-truck-inventory',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5d8fac37f749fe6a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/deliver-services/manage-service-truck-inventory'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/adaptive-card-manage-service-truck-inventory', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardManageServiceTruckInventory(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardManageServiceTruckInventory'
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
    print(AdaptiveCardManageServiceTruckInventory().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
