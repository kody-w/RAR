---
name: "rar-cowork-cookbook-adaptive-card-define-order-risk-management-strategy"
description: "Produces a reusable Adaptive Card JSON snapshot of define order risk management strategy status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_define_order_risk_management_strategy", "rar_sha256": "c1a0b88ddbe91765abe6096c473d93ee29983fa68191a0c0e568ab2042836032", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_define_order_risk_management_strategy_agent.py` and embedded as the fenced Python below (sha256 c1a0b88ddbe91765…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_define_order_risk_management_strategy_agent.py` first:

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
    "version": '2.0.0',
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
