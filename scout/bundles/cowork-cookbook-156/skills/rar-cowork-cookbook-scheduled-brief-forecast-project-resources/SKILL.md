---
name: "rar-cowork-cookbook-scheduled-brief-forecast-project-resources"
description: "Schedulable morning-brief email summarizing forecast project resources for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_forecast_project_resources", "rar_sha256": "c09a5a73244a571a46e0eade0b7e9f102f792f5576b82005c3cc99dd7ae05b16", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_forecast_project_resources`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_forecast_project_resources_agent.py` and in the RCI capsule.

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

Forecast project resources Scheduled Email Brief — Schedulable morning-brief email summarizing forecast project resources for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-forecast-project-resources
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_forecast_project_resources_agent.py` and embedded as the fenced Python below (sha256 c09a5a73244a571a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_forecast_project_resources_agent.py` first:

```bash
python3 scheduled_brief_forecast_project_resources_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_forecast_project_resources_agent.py   # or on stdin
python3 scheduled_brief_forecast_project_resources_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Forecast project resources Scheduled Email Brief — Schedulable morning-brief email summarizing forecast project resources for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-forecast-project-resources
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_forecast_project_resources',
    "version": '2.0.0',
    "display_name": 'Forecast project resources Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing forecast project resources for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-forecast-project-resources',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-forecast-project-resources',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2714468ab3e88ad9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/plan-projects/forecast-project-resources'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/scheduled-brief-forecast-project-resources', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ScheduledBriefForecastProjectResources(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefForecastProjectResources'
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
    print(ScheduledBriefForecastProjectResources().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
