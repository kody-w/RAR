---
name: "rar-cowork-cookbook-dashboard-define-order-risk-management-strategy"
description: "Produces a self-contained interactive HTML dashboard for define order risk management strategy - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_define_order_risk_management_strategy", "rar_sha256": "1622527f2b77156a621468ca43a02ad1a19029dd7f0acfcbd4b24f5298143e7d", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_define_order_risk_management_strategy_agent.py` and embedded as the fenced Python below (sha256 1622527f2b77156a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_define_order_risk_management_strategy_agent.py` first:

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
    "version": '2.0.1',
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
