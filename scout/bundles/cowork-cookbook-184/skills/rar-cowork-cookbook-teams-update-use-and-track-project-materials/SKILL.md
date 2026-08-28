---
name: "rar-cowork-cookbook-teams-update-use-and-track-project-materials"
description: "Drafts a Teams channel post on use and track project materials status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_use_and_track_project_materials", "rar_sha256": "5a1e175e57a910448ada38d607ec6621303e62ea8f3ed57afdac07d52963206e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_use_and_track_project_materials_agent.py` and embedded as the fenced Python below (sha256 5a1e175e57a91044…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_use_and_track_project_materials_agent.py` first:

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
    "version": '2.0.0',
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
