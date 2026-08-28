---
name: "rar-cowork-cookbook-dashboard-report-production-quality-non-conformance"
description: "Produces a self-contained interactive HTML dashboard for report production quality non-conformance - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_report_production_quality_non_conformance", "rar_sha256": "dc63c220171a91ba34a3490d2ac61f992c1a8c2d41e4b327bf9d69d690c32003", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_report_production_quality_non_conformance_agent.py` and embedded as the fenced Python below (sha256 dc63c220171a91ba…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_report_production_quality_non_conformance_agent.py` first:

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
    "version": '2.0.1',
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
