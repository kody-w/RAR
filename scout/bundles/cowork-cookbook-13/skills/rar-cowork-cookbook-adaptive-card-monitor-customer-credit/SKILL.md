---
name: "rar-cowork-cookbook-adaptive-card-monitor-customer-credit"
description: "Produces a reusable Adaptive Card JSON snapshot of monitor customer credit status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_monitor_customer_credit", "rar_sha256": "656745d70e09096030d91d860f4e01770380f08f58196858e1e34c96804617e0", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_monitor_customer_credit_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-monitor-customer-credit:292f03263180113ece2de0aa7731a9c1817fa0a4d3ce6706ba182d1e4753a708", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_monitor_customer_credit`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_monitor_customer_credit_agent.py` is
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

Monitor customer credit Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of monitor customer credit status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-monitor-customer-credit
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_monitor_customer_credit_agent.py` and embedded as the fenced Python below (sha256 656745d70e090960…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_monitor_customer_credit_agent.py` first:

```bash
python3 adaptive_card_monitor_customer_credit_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_monitor_customer_credit_agent.py   # or on stdin
python3 adaptive_card_monitor_customer_credit_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor customer credit Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of monitor customer credit status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-monitor-customer-credit
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_monitor_customer_credit',
    "version": '2.0.0',
    "display_name": 'Monitor customer credit Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of monitor customer credit status for embedding in dashboards, emails, or Teams.',
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
        "upstream_slug": 'adaptive-card-monitor-customer-credit',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-monitor-customer-credit',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5689a81c844dfba8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-credit-and-collections/monitor-customer-credit'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/adaptive-card-monitor-customer-credit', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardMonitorCustomerCredit(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardMonitorCustomerCredit'
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
    print(AdaptiveCardMonitorCustomerCredit().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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micAAA== -->
