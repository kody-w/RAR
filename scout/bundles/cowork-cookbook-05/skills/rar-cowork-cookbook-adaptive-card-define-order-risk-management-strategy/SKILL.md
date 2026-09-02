---
name: "rar-cowork-cookbook-adaptive-card-define-order-risk-management-strategy"
description: "Produces a reusable Adaptive Card JSON snapshot of define order risk management strategy status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_define_order_risk_management_strategy", "rar_sha256": "c1a0b88ddbe91765abe6096c473d93ee29983fa68191a0c0e568ab2042836032", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_define_order_risk_management_strategy_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-define-order-risk-management-strategy:61641044632d48baec1f9321655579df3eba6034fba1ac528eba85c7b66cbf4d", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_define_order_risk_management_strategy`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_define_order_risk_management_strategy_agent.py` is
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
