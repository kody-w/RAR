---
name: "rar-cowork-cookbook-dashboard-report-production-quality-non-conformance"
description: "Produces a self-contained interactive HTML dashboard for report production quality non-conformance - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_report_production_quality_non_conformance", "rar_sha256": "dbbec4ab6acaad4774f286fca6d8c153fd0c1650ed0c435a014c4717d3e31f19", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_report_production_quality_non_conformance_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-report-production-quality-non-conformance:6530d5af3817417c8e28800dffb1b522eb060ce93d23e7c68940601eed26a562", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_report_production_quality_non_conformance`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_report_production_quality_non_conformance_agent.py` is
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
