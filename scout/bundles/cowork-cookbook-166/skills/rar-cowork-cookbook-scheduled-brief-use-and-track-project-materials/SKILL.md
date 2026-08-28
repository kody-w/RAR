---
name: "rar-cowork-cookbook-scheduled-brief-use-and-track-project-materials"
description: "Schedulable morning-brief email summarizing use and track project materials for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_use_and_track_project_materials", "rar_sha256": "43dcb999511c4a404b79789be261748bf70f9e49793d147df237bb5622a12410", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_use_and_track_project_materials`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_use_and_track_project_materials_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_use_and_track_project_materials_agent.py` and embedded as the fenced Python below (sha256 43dcb999511c4a40…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_use_and_track_project_materials_agent.py` first:

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
    "version": '2.0.1',
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
