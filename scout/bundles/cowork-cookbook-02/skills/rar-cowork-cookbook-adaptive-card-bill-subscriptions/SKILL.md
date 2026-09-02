---
name: "rar-cowork-cookbook-adaptive-card-bill-subscriptions"
description: "Produces a reusable Adaptive Card JSON snapshot of bill subscriptions status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_bill_subscriptions", "rar_sha256": "b15abeb128afe3114623a32a1f6017e6be44d2bf758343a71df4313413037726", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_bill_subscriptions_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-bill-subscriptions:36d18919275798617ea928d63ba7a2089a684af034d07a487879cb6b3ce96a4b", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_bill_subscriptions`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_bill_subscriptions_agent.py` is
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_bill_subscriptions_agent.py` and embedded as the fenced Python below (sha256 b15abeb128afe311…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_bill_subscriptions_agent.py` first:

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
    "version": '2.0.0',
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
