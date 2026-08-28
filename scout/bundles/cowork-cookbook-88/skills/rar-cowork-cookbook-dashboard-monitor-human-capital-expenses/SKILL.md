---
name: "rar-cowork-cookbook-dashboard-monitor-human-capital-expenses"
description: "Produces a self-contained interactive HTML dashboard for monitor human capital expenses - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_monitor_human_capital_expenses", "rar_sha256": "a1007ceab247d77b90d51eeadefe021b7f65bca2594a2e38b95ecf803cfab4f6", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_monitor_human_capital_expenses`. The original RAPP
agent is preserved byte-for-byte in `dashboard_monitor_human_capital_expenses_agent.py` and in the RCI capsule.

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
