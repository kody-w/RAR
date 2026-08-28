---
name: "rar-cowork-cookbook-adaptive-card-adjust-inventory-levels"
description: "Produces a reusable Adaptive Card JSON snapshot of adjust inventory levels status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_adjust_inventory_levels", "rar_sha256": "2add617758d006a0c9ab61306e0cfd6791a3269b7a2eb9b29aa979aecd214b75", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_adjust_inventory_levels_agent.py` and embedded as the fenced Python below (sha256 2add617758d006a0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_adjust_inventory_levels_agent.py` first:

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
    "version": '2.0.0',
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
