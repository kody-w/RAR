---
name: "rar-cowork-cookbook-adaptive-card-load-goods-for-shipping"
description: "Produces a reusable Adaptive Card JSON snapshot of load goods for shipping status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_load_goods_for_shipping", "rar_sha256": "9a99aa7d74afeeb68ff75d137ba547ef7182aa99cd97b376c78aa9626a4e9536", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_load_goods_for_shipping_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-load-goods-for-shipping:c54a243098e0c4a737d3dc0ed07e01217d16072c39f50d3f6479177acd4c558f", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_load_goods_for_shipping`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_load_goods_for_shipping_agent.py` is
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
