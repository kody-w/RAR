---
name: "rar-cowork-cookbook-dashboard-forecast-maintenance"
description: "Produces a self-contained interactive HTML dashboard for forecast maintenance - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_forecast_maintenance", "rar_sha256": "02059bb70549058360c206ee3d050bb74d46a945f5b3402e5c1618152a44981c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_forecast_maintenance_agent.py` and embedded as the fenced Python below (sha256 02059bb705490583…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_forecast_maintenance_agent.py` first:

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
    "version": '2.0.0',
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
