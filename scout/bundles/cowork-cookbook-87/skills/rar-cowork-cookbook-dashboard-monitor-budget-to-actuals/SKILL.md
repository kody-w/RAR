---
name: "rar-cowork-cookbook-dashboard-monitor-budget-to-actuals"
description: "Produces a self-contained interactive HTML dashboard for monitor budget to actuals - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_monitor_budget_to_actuals", "rar_sha256": "8b9ebb5d18d019ec71c4c4cc412b1a85c5bd663a52b6aff04133bb0d1cf26ca9", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_monitor_budget_to_actuals`. The original RAPP
agent is preserved byte-for-byte in `dashboard_monitor_budget_to_actuals_agent.py` and in the RCI capsule.

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

Monitor budget to actuals Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for monitor budget to actuals - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-monitor-budget-to-actuals
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_monitor_budget_to_actuals_agent.py` and embedded as the fenced Python below (sha256 8b9ebb5d18d019ec…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_monitor_budget_to_actuals_agent.py` first:

```bash
python3 dashboard_monitor_budget_to_actuals_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_monitor_budget_to_actuals_agent.py   # or on stdin
python3 dashboard_monitor_budget_to_actuals_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor budget to actuals Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for monitor budget to actuals - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-monitor-budget-to-actuals
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_monitor_budget_to_actuals',
    "version": '2.0.1',
    "display_name": 'Monitor budget to actuals Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for monitor budget to actuals - opens in any browser, no D365 access needed by the viewer.',
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
        "upstream_slug": 'dashboard-monitor-budget-to-actuals',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-monitor-budget-to-actuals',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd6444f332a5bbec2',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/analyze-financial-performance/monitor-budget-to-actuals'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/dashboard-monitor-budget-to-actuals', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class DashboardMonitorBudgetToActuals(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardMonitorBudgetToActuals'
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
    print(DashboardMonitorBudgetToActuals().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
