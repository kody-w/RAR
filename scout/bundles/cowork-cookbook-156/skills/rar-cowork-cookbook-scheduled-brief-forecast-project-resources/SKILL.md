---
name: "rar-cowork-cookbook-scheduled-brief-forecast-project-resources"
description: "Schedulable morning-brief email summarizing forecast project resources for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_forecast_project_resources", "rar_sha256": "c09a5a73244a571a46e0eade0b7e9f102f792f5576b82005c3cc99dd7ae05b16", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_forecast_project_resources_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-forecast-project-resources:5e11988d641649bc16106f5e915385a5abd128cae39f1169399368da096a6426", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_forecast_project_resources`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_forecast_project_resources_agent.py` is
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
