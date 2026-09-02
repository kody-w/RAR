---
name: "rar-cowork-cookbook-teams-update-use-and-track-project-materials"
description: "Drafts a Teams channel post on use and track project materials status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_use_and_track_project_materials", "rar_sha256": "5a1e175e57a910448ada38d607ec6621303e62ea8f3ed57afdac07d52963206e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_use_and_track_project_materials_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-use-and-track-project-materials:a5e3f94706b4c47f5ef67f2b3ef09971653253bb7d453dc5aa8e3debb48a1e6a", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_use_and_track_project_materials`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_use_and_track_project_materials_agent.py` is
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
