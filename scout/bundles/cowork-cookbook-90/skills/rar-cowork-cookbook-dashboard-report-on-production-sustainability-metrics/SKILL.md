---
name: "rar-cowork-cookbook-dashboard-report-on-production-sustainability-metrics"
description: "Produces a self-contained interactive HTML dashboard for report on production sustainability metrics - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_report_on_production_sustainability_metrics", "rar_sha256": "26f8528d42d0cb4cbc426ded37c77d19738627bade280be65208a07a79cebc92", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_report_on_production_sustainability_metrics_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-report-on-production-sustainability-metrics:80e5e4d3e7c1836337cda42b8e1c21b1ace28de5496b88cfa1ae612a6761f98a", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_report_on_production_sustainability_metrics`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_report_on_production_sustainability_metrics_agent.py` is
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
