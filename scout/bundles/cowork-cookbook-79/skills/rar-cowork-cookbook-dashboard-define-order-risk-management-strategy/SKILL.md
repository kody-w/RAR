---
name: "rar-cowork-cookbook-dashboard-define-order-risk-management-strategy"
description: "Produces a self-contained interactive HTML dashboard for define order risk management strategy - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_define_order_risk_management_strategy", "rar_sha256": "343415bf341d3344c32a39499ac9806700cf4fd7825d340c8802d89a8712b4e9", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_define_order_risk_management_strategy`. The original RAPP
agent is preserved byte-for-byte in `dashboard_define_order_risk_management_strategy_agent.py` and in the RCI capsule.

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

Define order risk management strategy Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for define order risk management strategy - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-define-order-risk-management-strategy
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_define_order_risk_management_strategy_agent.py` and embedded as the fenced Python below (sha256 343415bf341d3344…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_define_order_risk_management_strategy_agent.py` first:

```bash
python3 dashboard_define_order_risk_management_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_define_order_risk_management_strategy_agent.py   # or on stdin
python3 dashboard_define_order_risk_management_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define order risk management strategy Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for define order risk management strategy - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-define-order-risk-management-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_define_order_risk_management_strategy',
    "version": '2.0.0',
    "display_name": 'Define order risk management strategy Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for define order risk management strategy - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-define-order-risk-management-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-define-order-risk-management-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '17952fe02394d3f8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/develop-sales-policies/define-order-risk-management-strategy'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/dashboard-define-order-risk-management-strategy', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardDefineOrderRiskManagementStrategy(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardDefineOrderRiskManagementStrategy'
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
    print(DashboardDefineOrderRiskManagementStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
