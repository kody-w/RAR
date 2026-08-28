---
name: "rar-cowork-cookbook-dashboard-report-on-production-sustainability-metrics"
description: "Produces a self-contained interactive HTML dashboard for report on production sustainability metrics - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_report_on_production_sustainability_metrics", "rar_sha256": "cc9bf8ac11663c476f5d71e6d7ffbba9efcbf169098a9503aa5fb1d24f81935d", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_report_on_production_sustainability_metrics`. The original RAPP
agent is preserved byte-for-byte in `dashboard_report_on_production_sustainability_metrics_agent.py` and in the RCI capsule.

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

Report on production sustainability metrics Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for report on production sustainability metrics - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-report-on-production-sustainability-metrics
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_report_on_production_sustainability_metrics_agent.py` and embedded as the fenced Python below (sha256 cc9bf8ac11663c47…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_report_on_production_sustainability_metrics_agent.py` first:

```bash
python3 dashboard_report_on_production_sustainability_metrics_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_report_on_production_sustainability_metrics_agent.py   # or on stdin
python3 dashboard_report_on_production_sustainability_metrics_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Report on production sustainability metrics Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for report on production sustainability metrics - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-report-on-production-sustainability-metrics
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_report_on_production_sustainability_metrics',
    "version": '2.0.1',
    "display_name": 'Report on production sustainability metrics Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for report on production sustainability metrics - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-report-on-production-sustainability-metrics',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-report-on-production-sustainability-metrics',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '71bf1fff7e8486c7',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/analyze-production-operations/report-on-production-sustainability-metrics'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/dashboard-report-on-production-sustainability-metrics', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DashboardReportOnProductionSustainabilityMetrics(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardReportOnProductionSustainabilityMetrics'
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
    print(DashboardReportOnProductionSustainabilityMetrics().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
