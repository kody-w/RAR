---
name: "rar-cowork-cookbook-dashboard-report-on-production-sustainability-metrics"
description: "Produces a self-contained interactive HTML dashboard for report on production sustainability metrics - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_report_on_production_sustainability_metrics", "rar_sha256": "26f8528d42d0cb4cbc426ded37c77d19738627bade280be65208a07a79cebc92", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_report_on_production_sustainability_metrics_agent.py` and embedded as the fenced Python below (sha256 26f8528d42d0cb4c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_report_on_production_sustainability_metrics_agent.py` first:

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
    "version": '2.0.0',
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
