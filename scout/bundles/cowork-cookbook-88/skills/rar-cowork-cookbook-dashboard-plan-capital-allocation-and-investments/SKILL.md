---
name: "rar-cowork-cookbook-dashboard-plan-capital-allocation-and-investments"
description: "Produces a self-contained interactive HTML dashboard for plan capital allocation and investments - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_plan_capital_allocation_and_investments", "rar_sha256": "afcc248fdea225eb70006023f0669d6141af4f01b9455b17ad4a9eefcb1f9927", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_plan_capital_allocation_and_investments`. The original RAPP
agent is preserved byte-for-byte in `dashboard_plan_capital_allocation_and_investments_agent.py` and in the RCI capsule.

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

Plan capital allocation and investments Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for plan capital allocation and investments - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-plan-capital-allocation-and-investments
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_plan_capital_allocation_and_investments_agent.py` and embedded as the fenced Python below (sha256 afcc248fdea225eb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_plan_capital_allocation_and_investments_agent.py` first:

```bash
python3 dashboard_plan_capital_allocation_and_investments_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_plan_capital_allocation_and_investments_agent.py   # or on stdin
python3 dashboard_plan_capital_allocation_and_investments_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan capital allocation and investments Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for plan capital allocation and investments - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-plan-capital-allocation-and-investments
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_plan_capital_allocation_and_investments',
    "version": '2.0.0',
    "display_name": 'Plan capital allocation and investments Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for plan capital allocation and investments - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-plan-capital-allocation-and-investments',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-plan-capital-allocation-and-investments',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ce632e5c71c176c6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-financial-planning/plan-capital-allocation-and-investments'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/dashboard-plan-capital-allocation-and-investments', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardPlanCapitalAllocationAndInvestments(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardPlanCapitalAllocationAndInvestments'
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
    print(DashboardPlanCapitalAllocationAndInvestments().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
