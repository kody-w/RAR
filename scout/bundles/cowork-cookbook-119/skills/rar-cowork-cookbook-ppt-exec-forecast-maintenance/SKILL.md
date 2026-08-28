---
name: "rar-cowork-cookbook-ppt-exec-forecast-maintenance"
description: "Generates an executive-ready PowerPoint deck on forecast maintenance status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_forecast_maintenance", "rar_sha256": "f350fceabbecdce62aa79d01265fc3b469f3fa09abb97c058ef3bb102360525e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_forecast_maintenance`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_forecast_maintenance_agent.py` and in the RCI capsule.

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

Forecast maintenance Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on forecast maintenance status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-forecast-maintenance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_forecast_maintenance_agent.py` and embedded as the fenced Python below (sha256 f350fceabbecdce6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_forecast_maintenance_agent.py` first:

```bash
python3 ppt_exec_forecast_maintenance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_forecast_maintenance_agent.py   # or on stdin
python3 ppt_exec_forecast_maintenance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Forecast maintenance Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on forecast maintenance status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-forecast-maintenance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_forecast_maintenance',
    "version": '2.0.0',
    "display_name": 'Forecast maintenance Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on forecast maintenance status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-forecast-maintenance',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-forecast-maintenance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd2dec7544506ee62',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/perform-asset-maintenance/forecast-maintenance'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/ppt-exec-forecast-maintenance', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class PptExecForecastMaintenance(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecForecastMaintenance'
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
    print(PptExecForecastMaintenance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
