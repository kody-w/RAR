---
name: "rar-cowork-cookbook-adaptive-card-adjust-inventory-levels"
description: "Produces a reusable Adaptive Card JSON snapshot of adjust inventory levels status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_adjust_inventory_levels", "rar_sha256": "368ca90aeb42af8a52ca502d8cbb91ee3312a39bc191a2b873d6c63ee08d9122", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_adjust_inventory_levels`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_adjust_inventory_levels_agent.py` and in the RCI capsule.

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

Adjust inventory levels Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of adjust inventory levels status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-adjust-inventory-levels
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_adjust_inventory_levels_agent.py` and embedded as the fenced Python below (sha256 368ca90aeb42af8a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_adjust_inventory_levels_agent.py` first:

```bash
python3 adaptive_card_adjust_inventory_levels_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_adjust_inventory_levels_agent.py   # or on stdin
python3 adaptive_card_adjust_inventory_levels_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Adjust inventory levels Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of adjust inventory levels status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-adjust-inventory-levels
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_adjust_inventory_levels',
    "version": '2.0.1',
    "display_name": 'Adjust inventory levels Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of adjust inventory levels status for embedding in dashboards, emails, or Teams.',
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
        "upstream_slug": 'adaptive-card-adjust-inventory-levels',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-adjust-inventory-levels',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2437b95c31d7167d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/maintain-inventory-levels/adjust-inventory-levels'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/adaptive-card-adjust-inventory-levels', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardAdjustInventoryLevels(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardAdjustInventoryLevels'
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
    print(AdaptiveCardAdjustInventoryLevels().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
