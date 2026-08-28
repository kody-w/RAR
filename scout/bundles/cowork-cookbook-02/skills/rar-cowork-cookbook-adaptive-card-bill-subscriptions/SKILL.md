---
name: "rar-cowork-cookbook-adaptive-card-bill-subscriptions"
description: "Produces a reusable Adaptive Card JSON snapshot of bill subscriptions status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_bill_subscriptions", "rar_sha256": "3c467912bf01079beea9409108ea406420fe7c6c2b2cdd7f91c8092fc250ca6a", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_bill_subscriptions`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_bill_subscriptions_agent.py` and in the RCI capsule.

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

Bill subscriptions Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of bill subscriptions status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-bill-subscriptions
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_bill_subscriptions_agent.py` and embedded as the fenced Python below (sha256 3c467912bf01079b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_bill_subscriptions_agent.py` first:

```bash
python3 adaptive_card_bill_subscriptions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_bill_subscriptions_agent.py   # or on stdin
python3 adaptive_card_bill_subscriptions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Bill subscriptions Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of bill subscriptions status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-bill-subscriptions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_bill_subscriptions',
    "version": '2.0.1',
    "display_name": 'Bill subscriptions Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of bill subscriptions status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-bill-subscriptions',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-bill-subscriptions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'fd20239a552a96db',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-accounts-receivable/bill-subscriptions'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/adaptive-card-bill-subscriptions', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardBillSubscriptions(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardBillSubscriptions'
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
    print(AdaptiveCardBillSubscriptions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
