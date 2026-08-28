---
name: "rar-cowork-cookbook-dashboard-report-on-compliance"
description: "Produces a self-contained interactive HTML dashboard for report on compliance - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_report_on_compliance", "rar_sha256": "c12888da867ac347054f67659e2aff90330a7467865b4e143337fbf3251ee1c0", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_report_on_compliance`. The original RAPP
agent is preserved byte-for-byte in `dashboard_report_on_compliance_agent.py` and in the RCI capsule.

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

Report on compliance Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for report on compliance - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-report-on-compliance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_report_on_compliance_agent.py` and embedded as the fenced Python below (sha256 c12888da867ac347…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_report_on_compliance_agent.py` first:

```bash
python3 dashboard_report_on_compliance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_report_on_compliance_agent.py   # or on stdin
python3 dashboard_report_on_compliance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Report on compliance Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for report on compliance - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-report-on-compliance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_report_on_compliance',
    "version": '2.0.0',
    "display_name": 'Report on compliance Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for report on compliance - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-report-on-compliance',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-report-on-compliance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4b1fb497491ec5f0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-compliance/report-on-compliance'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/dashboard-report-on-compliance', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardReportOnCompliance(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardReportOnCompliance'
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
    print(DashboardReportOnCompliance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
