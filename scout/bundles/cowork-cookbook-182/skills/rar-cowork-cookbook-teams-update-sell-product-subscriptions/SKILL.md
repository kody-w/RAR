---
name: "rar-cowork-cookbook-teams-update-sell-product-subscriptions"
description: "Drafts a Teams channel post on sell product subscriptions status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_sell_product_subscriptions", "rar_sha256": "6c713437d18eba109fa3390100bab460d9861694426b1b88347bae74b111be28", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_sell_product_subscriptions`. The original RAPP
agent is preserved byte-for-byte in `teams_update_sell_product_subscriptions_agent.py` and in the RCI capsule.

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

Sell product subscriptions Teams Channel Update — Drafts a Teams channel post on sell product subscriptions status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-sell-product-subscriptions
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_sell_product_subscriptions_agent.py` and embedded as the fenced Python below (sha256 6c713437d18eba10…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_sell_product_subscriptions_agent.py` first:

```bash
python3 teams_update_sell_product_subscriptions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_sell_product_subscriptions_agent.py   # or on stdin
python3 teams_update_sell_product_subscriptions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Sell product subscriptions Teams Channel Update — Drafts a Teams channel post on sell product subscriptions status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-sell-product-subscriptions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_sell_product_subscriptions',
    "version": '2.0.0',
    "display_name": 'Sell product subscriptions Teams Channel Update',
    "description": 'Drafts a Teams channel post on sell product subscriptions status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-sell-product-subscriptions',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-sell-product-subscriptions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '81059689d29b5243',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-sales-orders/sell-product-subscriptions'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/teams-update-sell-product-subscriptions', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class TeamsUpdateSellProductSubscriptions(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateSellProductSubscriptions'
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
    print(TeamsUpdateSellProductSubscriptions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
