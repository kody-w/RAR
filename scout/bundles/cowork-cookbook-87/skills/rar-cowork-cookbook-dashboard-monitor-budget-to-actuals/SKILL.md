---
name: "rar-cowork-cookbook-dashboard-monitor-budget-to-actuals"
description: "Produces a self-contained interactive HTML dashboard for monitor budget to actuals - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_monitor_budget_to_actuals", "rar_sha256": "f6f64c9ef778b4d05aab6cfdeb005abdf6086d7cbef806024b99b15327aa43cb", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_monitor_budget_to_actuals_agent.py` and embedded as the fenced Python below (sha256 f6f64c9ef778b4d0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_monitor_budget_to_actuals_agent.py` first:

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
    "version": '2.0.0',
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
