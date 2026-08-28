---
name: "rar-cowork-cookbook-dashboard-prepare-statutory-financial-reports"
description: "Produces a self-contained interactive HTML dashboard for prepare statutory financial reports - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_prepare_statutory_financial_reports", "rar_sha256": "fed863143b57e6966331d08ef0ae3616211fd858b248c44189f39ac8ff7156e6", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_prepare_statutory_financial_reports_agent.py` and embedded as the fenced Python below (sha256 fed863143b57e696…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_prepare_statutory_financial_reports_agent.py` first:

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
    "version": '2.0.0',
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
