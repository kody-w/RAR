---
name: "rar-cowork-cookbook-dashboard-plan-logistics-and-distribution"
description: "Produces a self-contained interactive HTML dashboard for plan logistics and distribution - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_plan_logistics_and_distribution", "rar_sha256": "506d31504a1563075a7e8dca1a26f109e072d3bcd0bf3eab716a73f295349cc3", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_plan_logistics_and_distribution_agent.py` and embedded as the fenced Python below (sha256 506d31504a156307…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_plan_logistics_and_distribution_agent.py` first:

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
    "version": '2.0.1',
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
