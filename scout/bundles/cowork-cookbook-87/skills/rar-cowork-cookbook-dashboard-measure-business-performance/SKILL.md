---
name: "rar-cowork-cookbook-dashboard-measure-business-performance"
description: "Produces a self-contained interactive HTML dashboard for measure business performance - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_measure_business_performance", "rar_sha256": "7771dde5df96c0dd5704a6d3b1e3e19b248e85eb94a672ab51dfeef2ba99c6c9", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_measure_business_performance`. The original RAPP
agent is preserved byte-for-byte in `dashboard_measure_business_performance_agent.py` and in the RCI capsule.

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

Measure business performance Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for measure business performance - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-measure-business-performance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_measure_business_performance_agent.py` and embedded as the fenced Python below (sha256 7771dde5df96c0dd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_measure_business_performance_agent.py` first:

```bash
python3 dashboard_measure_business_performance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_measure_business_performance_agent.py   # or on stdin
python3 dashboard_measure_business_performance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Measure business performance Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for measure business performance - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-measure-business-performance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_measure_business_performance',
    "version": '2.0.1',
    "display_name": 'Measure business performance Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for measure business performance - opens in any browser, no D365 access needed by the viewer.',
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
        "upstream_slug": 'dashboard-measure-business-performance',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-measure-business-performance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '91048919d59346b6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/analyze-business-performance/measure-business-performance'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/dashboard-measure-business-performance', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardMeasureBusinessPerformance(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardMeasureBusinessPerformance'
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
    print(DashboardMeasureBusinessPerformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
