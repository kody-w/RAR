---
name: "rar-cowork-cookbook-dashboard-plan-logistics-and-distribution"
description: "Produces a self-contained interactive HTML dashboard for plan logistics and distribution - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_plan_logistics_and_distribution", "rar_sha256": "c78deeed5e0b13d665847404803d971521deeeb5d6f7dc40bce5864b1c7f760c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_plan_logistics_and_distribution`. The original RAPP
agent is preserved byte-for-byte in `dashboard_plan_logistics_and_distribution_agent.py` and in the RCI capsule.

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

Plan logistics and distribution Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for plan logistics and distribution - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-plan-logistics-and-distribution
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_plan_logistics_and_distribution_agent.py` and embedded as the fenced Python below (sha256 c78deeed5e0b13d6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_plan_logistics_and_distribution_agent.py` first:

```bash
python3 dashboard_plan_logistics_and_distribution_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_plan_logistics_and_distribution_agent.py   # or on stdin
python3 dashboard_plan_logistics_and_distribution_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan logistics and distribution Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for plan logistics and distribution - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-plan-logistics-and-distribution
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_plan_logistics_and_distribution',
    "version": '2.0.0',
    "display_name": 'Plan logistics and distribution Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for plan logistics and distribution - opens in any browser, no D365 access needed by the viewer.',
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
        "upstream_slug": 'dashboard-plan-logistics-and-distribution',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-plan-logistics-and-distribution',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '33f2c6d250e964d7',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/execute-sales-and-operations/plan-logistics-and-distribution'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/dashboard-plan-logistics-and-distribution', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardPlanLogisticsAndDistribution(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardPlanLogisticsAndDistribution'
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
    print(DashboardPlanLogisticsAndDistribution().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
