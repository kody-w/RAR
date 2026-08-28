---
name: "rar-cowork-cookbook-adaptive-card-define-order-risk-management-strategy"
description: "Produces a reusable Adaptive Card JSON snapshot of define order risk management strategy status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_define_order_risk_management_strategy", "rar_sha256": "a35d8de233059da864ede66ba3e0b60cfe5aa02a0d4ef67cc632d6a9c085469a", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_define_order_risk_management_strategy`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_define_order_risk_management_strategy_agent.py` and in the RCI capsule.

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

Define order risk management strategy Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of define order risk management strategy status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-define-order-risk-management-strategy
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_define_order_risk_management_strategy_agent.py` and embedded as the fenced Python below (sha256 a35d8de233059da8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_define_order_risk_management_strategy_agent.py` first:

```bash
python3 adaptive_card_define_order_risk_management_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_define_order_risk_management_strategy_agent.py   # or on stdin
python3 adaptive_card_define_order_risk_management_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define order risk management strategy Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of define order risk management strategy status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-define-order-risk-management-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_define_order_risk_management_strategy',
    "version": '2.0.1',
    "display_name": 'Define order risk management strategy Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of define order risk management strategy status for embedding in dashboards, emails, or Teams.',
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
        "upstream_slug": 'adaptive-card-define-order-risk-management-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-define-order-risk-management-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0a7dfa4cb70edc10',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/develop-sales-policies/define-order-risk-management-strategy'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/adaptive-card-define-order-risk-management-strategy', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class AdaptiveCardDefineOrderRiskManagementStrategy(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardDefineOrderRiskManagementStrategy'
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
    print(AdaptiveCardDefineOrderRiskManagementStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
