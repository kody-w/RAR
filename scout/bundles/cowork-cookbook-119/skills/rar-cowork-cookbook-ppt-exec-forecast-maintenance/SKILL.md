---
name: "rar-cowork-cookbook-ppt-exec-forecast-maintenance"
description: "Generates an executive-ready PowerPoint deck on forecast maintenance status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_forecast_maintenance", "rar_sha256": "6f0e3e6ac3ec3942fc16ddcfa11ee70efb3f4eb42ad67174573d4c4b44a46b6e", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_forecast_maintenance_agent.py` and embedded as the fenced Python below (sha256 6f0e3e6ac3ec3942…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_forecast_maintenance_agent.py` first:

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
    "version": '2.0.1',
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
