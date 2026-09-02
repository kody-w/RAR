---
name: "rar-cowork-cookbook-scheduled-brief-use-and-track-project-materials"
description: "Schedulable morning-brief email summarizing use and track project materials for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_use_and_track_project_materials", "rar_sha256": "b88bcf9b7539d36445ed6e7d78210f0b5af7bccc8c2582075f97023f6c1d58c9", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_use_and_track_project_materials_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-use-and-track-project-materials:65bc4bba36e2d066458f18bfdae8a9a8ebe097564e432ad83a234248de3557c7", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_use_and_track_project_materials`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_use_and_track_project_materials_agent.py` is
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

Use and track project materials Scheduled Email Brief — Schedulable morning-brief email summarizing use and track project materials for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-use-and-track-project-materials
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_use_and_track_project_materials_agent.py` and embedded as the fenced Python below (sha256 b88bcf9b7539d364…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_use_and_track_project_materials_agent.py` first:

```bash
python3 scheduled_brief_use_and_track_project_materials_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_use_and_track_project_materials_agent.py   # or on stdin
python3 scheduled_brief_use_and_track_project_materials_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Use and track project materials Scheduled Email Brief — Schedulable morning-brief email summarizing use and track project materials for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-use-and-track-project-materials
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_use_and_track_project_materials',
    "version": '2.0.0',
    "display_name": 'Use and track project materials Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing use and track project materials for the responsible owner; designed to run daily or weekly.',
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
        "upstream_slug": 'scheduled-brief-use-and-track-project-materials',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-use-and-track-project-materials',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a344676db4f4fb5d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-delivery/use-and-track-project-materials'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/scheduled-brief-use-and-track-project-materials', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefUseAndTrackProjectMaterials(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefUseAndTrackProjectMaterials'
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
    print(ScheduledBriefUseAndTrackProjectMaterials().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
