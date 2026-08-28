---
name: "rar-cowork-cookbook-adaptive-card-load-goods-for-shipping"
description: "Produces a reusable Adaptive Card JSON snapshot of load goods for shipping status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_load_goods_for_shipping", "rar_sha256": "f8778cb645eb71e5acac5d09c6c20b2b021efaceb1394f9633d47b684f216465", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_load_goods_for_shipping`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_load_goods_for_shipping_agent.py` and in the RCI capsule.

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

Load goods for shipping Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of load goods for shipping status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-load-goods-for-shipping
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_load_goods_for_shipping_agent.py` and embedded as the fenced Python below (sha256 f8778cb645eb71e5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_load_goods_for_shipping_agent.py` first:

```bash
python3 adaptive_card_load_goods_for_shipping_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_load_goods_for_shipping_agent.py   # or on stdin
python3 adaptive_card_load_goods_for_shipping_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Load goods for shipping Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of load goods for shipping status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-load-goods-for-shipping
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_load_goods_for_shipping',
    "version": '2.0.1',
    "display_name": 'Load goods for shipping Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of load goods for shipping status for embedding in dashboards, emails, or Teams.',
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
        "upstream_slug": 'adaptive-card-load-goods-for-shipping',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-load-goods-for-shipping',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '642f173f67c7aaa5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/process-outbound-goods/load-goods-for-shipping'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/adaptive-card-load-goods-for-shipping', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardLoadGoodsForShipping(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardLoadGoodsForShipping'
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
    print(AdaptiveCardLoadGoodsForShipping().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
