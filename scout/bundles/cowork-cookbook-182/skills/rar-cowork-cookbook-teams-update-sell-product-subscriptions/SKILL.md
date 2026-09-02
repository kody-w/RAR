---
name: "rar-cowork-cookbook-teams-update-sell-product-subscriptions"
description: "Drafts a Teams channel post on sell product subscriptions status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_sell_product_subscriptions", "rar_sha256": "6c713437d18eba109fa3390100bab460d9861694426b1b88347bae74b111be28", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_sell_product_subscriptions_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-sell-product-subscriptions:c1920a77bf1d12ce06fac09d9e55a7a1da08a70782ebbc82230cfff222c9b065", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_sell_product_subscriptions`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_sell_product_subscriptions_agent.py` is
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
