---
name: "rar-cowork-cookbook-dashboard-monitor-human-capital-expenses"
description: "Produces a self-contained interactive HTML dashboard for monitor human capital expenses - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_monitor_human_capital_expenses", "rar_sha256": "a1007ceab247d77b90d51eeadefe021b7f65bca2594a2e38b95ecf803cfab4f6", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_monitor_human_capital_expenses_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-monitor-human-capital-expenses:0fa8369a387d4d47668051d2c7cfdb1c193d7a06d123971db36630803c513149", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_monitor_human_capital_expenses`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_monitor_human_capital_expenses_agent.py` is
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

Monitor human capital expenses Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for monitor human capital expenses - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-monitor-human-capital-expenses
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_monitor_human_capital_expenses_agent.py` and embedded as the fenced Python below (sha256 a1007ceab247d77b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_monitor_human_capital_expenses_agent.py` first:

```bash
python3 dashboard_monitor_human_capital_expenses_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_monitor_human_capital_expenses_agent.py   # or on stdin
python3 dashboard_monitor_human_capital_expenses_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor human capital expenses Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for monitor human capital expenses - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-monitor-human-capital-expenses
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_monitor_human_capital_expenses',
    "version": '2.0.0',
    "display_name": 'Monitor human capital expenses Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for monitor human capital expenses - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-monitor-human-capital-expenses',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-monitor-human-capital-expenses',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'fedf2a355ddc3d6e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/analyze-hr-programs/monitor-human-capital-expenses'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/dashboard-monitor-human-capital-expenses', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardMonitorHumanCapitalExpenses(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardMonitorHumanCapitalExpenses'
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
    print(DashboardMonitorHumanCapitalExpenses().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
