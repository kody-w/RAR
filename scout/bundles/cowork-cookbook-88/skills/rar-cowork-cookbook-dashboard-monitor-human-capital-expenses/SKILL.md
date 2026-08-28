---
name: "rar-cowork-cookbook-dashboard-monitor-human-capital-expenses"
description: "Produces a self-contained interactive HTML dashboard for monitor human capital expenses - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_monitor_human_capital_expenses", "rar_sha256": "1203fd160decbef082577e516bd944c33bf51c34ed64f23486f25905e5f3a156", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_monitor_human_capital_expenses_agent.py` and embedded as the fenced Python below (sha256 1203fd160decbef0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_monitor_human_capital_expenses_agent.py` first:

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
    "version": '2.0.1',
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
