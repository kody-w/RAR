---
name: "rar-cowork-cookbook-ppt-exec-forecast-maintenance"
description: "Generates an executive-ready PowerPoint deck on forecast maintenance status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_forecast_maintenance", "rar_sha256": "f350fceabbecdce62aa79d01265fc3b469f3fa09abb97c058ef3bb102360525e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_forecast_maintenance_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-forecast-maintenance:64c629434d218132ce2e2e083b686f97ad9ec9fb4dab339bd83d983460152aba", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_forecast_maintenance`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_forecast_maintenance_agent.py` is
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
