---
name: "rar-cowork-cookbook-teams-update-forecast-project-resources"
description: "Drafts a Teams channel post on forecast project resources status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_forecast_project_resources", "rar_sha256": "815927b78dc6f74b648d3d46589322148bbc7cfc1700039c9f2b3902f880651a", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_forecast_project_resources`. The original RAPP
agent is preserved byte-for-byte in `teams_update_forecast_project_resources_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_forecast_project_resources_agent.py` and embedded as the fenced Python below (sha256 815927b78dc6f74b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_forecast_project_resources_agent.py` first:

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
    "version": '2.0.1',
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
