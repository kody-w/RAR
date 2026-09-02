---
name: "rar-cowork-cookbook-teams-update-forecast-project-resources"
description: "Drafts a Teams channel post on forecast project resources status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_forecast_project_resources", "rar_sha256": "fbca85db68f707b8495fd68431268869d02277419901f13d330f900df61abad8", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_forecast_project_resources_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-forecast-project-resources:b51adb873bb88d99ef3bac0cfc3ca8fd4518f4da40be5043ec714a13f39f7bc2", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_forecast_project_resources`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_forecast_project_resources_agent.py` is
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

Forecast project resources Teams Channel Update — Drafts a Teams channel post on forecast project resources status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-forecast-project-resources
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_forecast_project_resources_agent.py` and embedded as the fenced Python below (sha256 fbca85db68f707b8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_forecast_project_resources_agent.py` first:

```bash
python3 teams_update_forecast_project_resources_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_forecast_project_resources_agent.py   # or on stdin
python3 teams_update_forecast_project_resources_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Forecast project resources Teams Channel Update — Drafts a Teams channel post on forecast project resources status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-forecast-project-resources
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_forecast_project_resources',
    "version": '2.0.0',
    "display_name": 'Forecast project resources Teams Channel Update',
    "description": 'Drafts a Teams channel post on forecast project resources status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-forecast-project-resources',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-forecast-project-resources',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '362660ba24797920',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/plan-projects/forecast-project-resources'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/teams-update-forecast-project-resources', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateForecastProjectResources(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateForecastProjectResources'
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
    print(TeamsUpdateForecastProjectResources().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
