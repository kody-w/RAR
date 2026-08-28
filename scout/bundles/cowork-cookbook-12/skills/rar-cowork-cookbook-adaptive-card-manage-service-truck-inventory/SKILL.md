---
name: "rar-cowork-cookbook-adaptive-card-manage-service-truck-inventory"
description: "Produces a reusable Adaptive Card JSON snapshot of manage service truck inventory status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_manage_service_truck_inventory", "rar_sha256": "d02066e8a31ba6ff28507b3132d876259972f1376761944d4871f9370409e56e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_manage_service_truck_inventory_agent.py` and embedded as the fenced Python below (sha256 d02066e8a31ba6ff…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_manage_service_truck_inventory_agent.py` first:

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
    "version": '2.0.0',
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
