---
name: "rar-cowork-cookbook-dashboard-measure-business-performance"
description: "Produces a self-contained interactive HTML dashboard for measure business performance - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_measure_business_performance", "rar_sha256": "33ea5c3cce6f7b00516ecfb9ec3d8eae5a32b8df6bdc16e74cbb2cda373c4442", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_measure_business_performance_agent.py` and embedded as the fenced Python below (sha256 33ea5c3cce6f7b00…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_measure_business_performance_agent.py` first:

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
    "version": '2.0.0',
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
