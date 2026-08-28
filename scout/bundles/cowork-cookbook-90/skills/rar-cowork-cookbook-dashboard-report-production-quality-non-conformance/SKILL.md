---
name: "rar-cowork-cookbook-dashboard-report-production-quality-non-conformance"
description: "Produces a self-contained interactive HTML dashboard for report production quality non-conformance - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_report_production_quality_non_conformance", "rar_sha256": "dbbec4ab6acaad4774f286fca6d8c153fd0c1650ed0c435a014c4717d3e31f19", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_report_production_quality_non_conformance`. The original RAPP
agent is preserved byte-for-byte in `dashboard_report_production_quality_non_conformance_agent.py` and in the RCI capsule.

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

Report production quality non-conformance Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for report production quality non-conformance - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-report-production-quality-non-conformance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_report_production_quality_non_conformance_agent.py` and embedded as the fenced Python below (sha256 dbbec4ab6acaad47…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_report_production_quality_non_conformance_agent.py` first:

```bash
python3 dashboard_report_production_quality_non_conformance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_report_production_quality_non_conformance_agent.py   # or on stdin
python3 dashboard_report_production_quality_non_conformance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Report production quality non-conformance Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for report production quality non-conformance - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-report-production-quality-non-conformance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_report_production_quality_non_conformance',
    "version": '2.0.0',
    "display_name": 'Report production quality non-conformance Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for report production quality non-conformance - opens in any browser, no D365 access needed by the viewer.',
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
        "upstream_slug": 'dashboard-report-production-quality-non-conformance',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-report-production-quality-non-conformance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7adfc80829cf1fa3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/control-production-quality/report-production-quality-non-conformance'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/dashboard-report-production-quality-non-conformance', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardReportProductionQualityNonConformance(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardReportProductionQualityNonConformance'
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
    print(DashboardReportProductionQualityNonConformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
