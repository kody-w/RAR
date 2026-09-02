---
name: "rar-cowork-cookbook-dashboard-report-on-compliance"
description: "Produces a self-contained interactive HTML dashboard for report on compliance - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_report_on_compliance", "rar_sha256": "c12888da867ac347054f67659e2aff90330a7467865b4e143337fbf3251ee1c0", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_report_on_compliance_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-report-on-compliance:14340a64997ba71bf31d14cf8b10e58e2ea643aaccbb897af62807d7b2659a50", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_report_on_compliance`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_report_on_compliance_agent.py` is
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
