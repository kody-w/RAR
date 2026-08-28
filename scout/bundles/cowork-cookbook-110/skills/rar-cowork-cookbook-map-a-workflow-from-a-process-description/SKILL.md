---
name: "rar-cowork-cookbook-map-a-workflow-from-a-process-description"
description: "Make a workflow shareable, reviewable, and improvable - without spending hours building the diagram by hand."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/map_a_workflow_from_a_process_description", "rar_sha256": "0d0a41ac1f93ad70ee1888a8e2f655d7402f7f0b020975dad3b6d477afb61cbb", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "work_management", "beginner", "integration", "miro"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/map_a_workflow_from_a_process_description`. The original RAPP
agent is preserved byte-for-byte in `map_a_workflow_from_a_process_description_agent.py` and in the RCI capsule.

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

Map a workflow from a process description — Make a workflow shareable, reviewable, and improvable - without spending hours building the diagram by hand.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/map-a-workflow-from-a-process-description
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `map_a_workflow_from_a_process_description_agent.py` and embedded as the fenced Python below (sha256 0d0a41ac1f93ad70…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `map_a_workflow_from_a_process_description_agent.py` first:

```bash
python3 map_a_workflow_from_a_process_description_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 map_a_workflow_from_a_process_description_agent.py   # or on stdin
python3 map_a_workflow_from_a_process_description_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Map a workflow from a process description — Make a workflow shareable, reviewable, and improvable - without spending hours building the diagram by hand.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/map-a-workflow-from-a-process-description
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/map_a_workflow_from_a_process_description',
    "version": '2.0.1',
    "display_name": 'Map a workflow from a process description',
    "description": 'Make a workflow shareable, reviewable, and improvable - without spending hours building the diagram by hand.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'work_management', 'beginner', 'integration', 'miro'],
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
        "upstream_slug": 'map-a-workflow-from-a-process-description',
        "upstream_url": 'https://coworkcookbook.com/recipes/map-a-workflow-from-a-process-description',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2a1cc4e37c979b34',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'beginner', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'miro', 'process_roots': ['work-management'], 'process_tags': ['work-management/create-and-repurpose-content/diagram-processes-and-workflows'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'work-management/map-a-workflow-from-a-process-description', 'uses_skills': {'custom': [], 'ootb': ['Meetings'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'word:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class MapAWorkflowFromAProcessDescription(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'MapAWorkflowFromAProcessDescription'
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
    print(MapAWorkflowFromAProcessDescription().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
