---
name: "rar-cowork-cookbook-dashboard-prepare-statutory-financial-reports"
description: "Produces a self-contained interactive HTML dashboard for prepare statutory financial reports - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_prepare_statutory_financial_reports", "rar_sha256": "77125c31cbe7f2f920078f1f7d19f31f5496832ea466f5026e03f73cb9791d35", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_prepare_statutory_financial_reports`. The original RAPP
agent is preserved byte-for-byte in `dashboard_prepare_statutory_financial_reports_agent.py` and in the RCI capsule.

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

Prepare statutory financial reports Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for prepare statutory financial reports - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-prepare-statutory-financial-reports
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_prepare_statutory_financial_reports_agent.py` and embedded as the fenced Python below (sha256 77125c31cbe7f2f9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_prepare_statutory_financial_reports_agent.py` first:

```bash
python3 dashboard_prepare_statutory_financial_reports_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_prepare_statutory_financial_reports_agent.py   # or on stdin
python3 dashboard_prepare_statutory_financial_reports_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Prepare statutory financial reports Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for prepare statutory financial reports - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-prepare-statutory-financial-reports
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_prepare_statutory_financial_reports',
    "version": '2.0.1',
    "display_name": 'Prepare statutory financial reports Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for prepare statutory financial reports - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'dashboard-prepare-statutory-financial-reports',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-prepare-statutory-financial-reports',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ccb9256a0f20f88b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/close-financial-periods/prepare-statutory-financial-reports'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/dashboard-prepare-statutory-financial-reports', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class DashboardPrepareStatutoryFinancialReports(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardPrepareStatutoryFinancialReports'
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
    print(DashboardPrepareStatutoryFinancialReports().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
