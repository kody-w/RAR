---
name: "rar-cowork-cookbook-dashboard-forecast-maintenance"
description: "Produces a self-contained interactive HTML dashboard for forecast maintenance - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_forecast_maintenance", "rar_sha256": "02059bb70549058360c206ee3d050bb74d46a945f5b3402e5c1618152a44981c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_forecast_maintenance_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-forecast-maintenance:3dbd132953fcb73023a9637e5447d93e21f2534b1544a70ea3ec6f85c97ebbe3", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_forecast_maintenance`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_forecast_maintenance_agent.py` is
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
