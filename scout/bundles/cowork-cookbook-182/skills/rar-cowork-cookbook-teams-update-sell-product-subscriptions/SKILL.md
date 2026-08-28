---
name: "rar-cowork-cookbook-teams-update-sell-product-subscriptions"
description: "Drafts a Teams channel post on sell product subscriptions status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_sell_product_subscriptions", "rar_sha256": "c7b7c491961dd123380fb7d6ffffe2aa6db8e37447b0694b54c71483c034f5c7", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_sell_product_subscriptions_agent.py` and embedded as the fenced Python below (sha256 c7b7c491961dd123…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_sell_product_subscriptions_agent.py` first:

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
    "version": '2.0.1',
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
