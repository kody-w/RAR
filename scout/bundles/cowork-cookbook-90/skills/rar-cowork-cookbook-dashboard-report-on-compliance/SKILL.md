---
name: "rar-cowork-cookbook-dashboard-report-on-compliance"
description: "Produces a self-contained interactive HTML dashboard for report on compliance - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_report_on_compliance", "rar_sha256": "2aa1126f6afb797334a6a8aa4ebd57bac9ca1375ecabec09edd431e0a12141a2", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_report_on_compliance_agent.py` and embedded as the fenced Python below (sha256 2aa1126f6afb7973…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_report_on_compliance_agent.py` first:

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
    "version": '2.0.1',
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
