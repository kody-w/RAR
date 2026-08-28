---
name: "rar-cowork-cookbook-dashboard-forecast-maintenance"
description: "Produces a self-contained interactive HTML dashboard for forecast maintenance - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_forecast_maintenance", "rar_sha256": "2a9c3c548701a4dd7bef79dbcb0a5412fc32ba13f1933d0ca7d4888f9c7a0cc4", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_forecast_maintenance`. The original RAPP
agent is preserved byte-for-byte in `dashboard_forecast_maintenance_agent.py` and in the RCI capsule.

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

Forecast maintenance Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for forecast maintenance - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-forecast-maintenance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_forecast_maintenance_agent.py` and embedded as the fenced Python below (sha256 2a9c3c548701a4dd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_forecast_maintenance_agent.py` first:

```bash
python3 dashboard_forecast_maintenance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_forecast_maintenance_agent.py   # or on stdin
python3 dashboard_forecast_maintenance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Forecast maintenance Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for forecast maintenance - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-forecast-maintenance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_forecast_maintenance',
    "version": '2.0.1',
    "display_name": 'Forecast maintenance Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for forecast maintenance - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-forecast-maintenance',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-forecast-maintenance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '354b75253f63c502',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/perform-asset-maintenance/forecast-maintenance'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/dashboard-forecast-maintenance', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class DashboardForecastMaintenance(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardForecastMaintenance'
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
    print(DashboardForecastMaintenance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
