---
name: "rar-cowork-cookbook-adaptive-card-monitor-customer-credit"
description: "Produces a reusable Adaptive Card JSON snapshot of monitor customer credit status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_monitor_customer_credit", "rar_sha256": "656745d70e09096030d91d860f4e01770380f08f58196858e1e34c96804617e0", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_monitor_customer_credit`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_monitor_customer_credit_agent.py` and in the RCI capsule.

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

<!-- rci-capsule:v1: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 -->
