---
name: "rar-cowork-cookbook-dashboard-plan-capital-allocation-and-investments"
description: "Produces a self-contained interactive HTML dashboard for plan capital allocation and investments - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_plan_capital_allocation_and_investments", "rar_sha256": "afcc248fdea225eb70006023f0669d6141af4f01b9455b17ad4a9eefcb1f9927", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_plan_capital_allocation_and_investments_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-plan-capital-allocation-and-investments:fc6c65cd97a3ecb96339fc658fa93d911514dd65160983abfcdd7ceca2d8594e", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_plan_capital_allocation_and_investments`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_plan_capital_allocation_and_investments_agent.py` is
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
