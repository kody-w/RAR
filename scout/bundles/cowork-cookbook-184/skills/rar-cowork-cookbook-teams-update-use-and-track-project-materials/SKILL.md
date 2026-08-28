---
name: "rar-cowork-cookbook-teams-update-use-and-track-project-materials"
description: "Drafts a Teams channel post on use and track project materials status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_use_and_track_project_materials", "rar_sha256": "919aabad142d45a5017a9c872840e0170e3f23f88df1686f6f6786348c497fe2", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_use_and_track_project_materials`. The original RAPP
agent is preserved byte-for-byte in `teams_update_use_and_track_project_materials_agent.py` and in the RCI capsule.

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

Use and track project materials Teams Channel Update — Drafts a Teams channel post on use and track project materials status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-use-and-track-project-materials
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_use_and_track_project_materials_agent.py` and embedded as the fenced Python below (sha256 919aabad142d45a5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_use_and_track_project_materials_agent.py` first:

```bash
python3 teams_update_use_and_track_project_materials_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_use_and_track_project_materials_agent.py   # or on stdin
python3 teams_update_use_and_track_project_materials_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Use and track project materials Teams Channel Update — Drafts a Teams channel post on use and track project materials status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-use-and-track-project-materials
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_use_and_track_project_materials',
    "version": '2.0.1',
    "display_name": 'Use and track project materials Teams Channel Update',
    "description": 'Drafts a Teams channel post on use and track project materials status with an interactive Adaptive Card for quick triage.',
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
        "upstream_slug": 'teams-update-use-and-track-project-materials',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-use-and-track-project-materials',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f460387199ac1674',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-delivery/use-and-track-project-materials'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/teams-update-use-and-track-project-materials', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateUseAndTrackProjectMaterials(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateUseAndTrackProjectMaterials'
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
    print(TeamsUpdateUseAndTrackProjectMaterials().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
