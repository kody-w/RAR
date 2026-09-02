---
name: "rar-cowork-cookbook-dashboard-define-order-risk-management-strategy"
description: "Produces a self-contained interactive HTML dashboard for define order risk management strategy - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_define_order_risk_management_strategy", "rar_sha256": "343415bf341d3344c32a39499ac9806700cf4fd7825d340c8802d89a8712b4e9", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_define_order_risk_management_strategy_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-define-order-risk-management-strategy:e33e43f1c4c9a07af285b5da150c9f7894cd764eb2a4914bd6b0af1b262ea56c", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_define_order_risk_management_strategy`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_define_order_risk_management_strategy_agent.py` is
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
