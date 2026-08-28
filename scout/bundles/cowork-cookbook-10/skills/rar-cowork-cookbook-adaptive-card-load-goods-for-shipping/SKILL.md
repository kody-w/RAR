---
name: "rar-cowork-cookbook-adaptive-card-load-goods-for-shipping"
description: "Produces a reusable Adaptive Card JSON snapshot of load goods for shipping status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_load_goods_for_shipping", "rar_sha256": "9a99aa7d74afeeb68ff75d137ba547ef7182aa99cd97b376c78aa9626a4e9536", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_load_goods_for_shipping_agent.py` and embedded as the fenced Python below (sha256 9a99aa7d74afeeb6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_load_goods_for_shipping_agent.py` first:

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
    "version": '2.0.0',
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
