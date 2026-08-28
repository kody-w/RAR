---
name: "rar-cowork-cookbook-scheduled-brief-use-and-track-project-materials"
description: "Schedulable morning-brief email summarizing use and track project materials for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_use_and_track_project_materials", "rar_sha256": "b88bcf9b7539d36445ed6e7d78210f0b5af7bccc8c2582075f97023f6c1d58c9", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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
