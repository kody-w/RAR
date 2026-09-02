---
name: "rar-cowork-cookbook-dashboard-monitor-budget-to-actuals"
description: "Produces a self-contained interactive HTML dashboard for monitor budget to actuals - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_monitor_budget_to_actuals", "rar_sha256": "f6f64c9ef778b4d05aab6cfdeb005abdf6086d7cbef806024b99b15327aa43cb", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_monitor_budget_to_actuals_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-monitor-budget-to-actuals:9f9660e97b27d2bb80ca3af5420d45c2ee8ad92ff986cdcaab8273a1df45805a", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_monitor_budget_to_actuals`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_monitor_budget_to_actuals_agent.py` is
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
