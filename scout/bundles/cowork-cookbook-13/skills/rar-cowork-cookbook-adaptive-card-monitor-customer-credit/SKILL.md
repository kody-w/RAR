---
name: "rar-cowork-cookbook-adaptive-card-monitor-customer-credit"
description: "Produces a reusable Adaptive Card JSON snapshot of monitor customer credit status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_monitor_customer_credit", "rar_sha256": "43ce7aa69323d77d7632847f4952fddfbe4e95db5de8f8379cfe279864599be4", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_monitor_customer_credit_agent.py` and embedded as the fenced Python below (sha256 43ce7aa69323d77d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_monitor_customer_credit_agent.py` first:

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
    "version": '2.0.1',
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
