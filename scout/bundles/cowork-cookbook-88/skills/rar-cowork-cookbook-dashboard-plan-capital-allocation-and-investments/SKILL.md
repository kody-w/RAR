---
name: "rar-cowork-cookbook-dashboard-plan-capital-allocation-and-investments"
description: "Produces a self-contained interactive HTML dashboard for plan capital allocation and investments - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_plan_capital_allocation_and_investments", "rar_sha256": "8f037e3f85b27f76641c03b62679d37259d6c56f4e8f90938de49f1e6e55f5a2", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_plan_capital_allocation_and_investments_agent.py` and embedded as the fenced Python below (sha256 8f037e3f85b27f76…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_plan_capital_allocation_and_investments_agent.py` first:

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
    "version": '2.0.1',
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
