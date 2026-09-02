---
name: "rar-cowork-cookbook-map-a-workflow-from-a-process-description"
description: "Make a workflow shareable, reviewable, and improvable - without spending hours building the diagram by hand."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/map_a_workflow_from_a_process_description", "rar_sha256": "f2bc882e02104c377f714e9db4d24699caf74d79bf15064b7ba5a81062103adb", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "map_a_workflow_from_a_process_description_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/map-a-workflow-from-a-process-description:e5bdbfa5343eca99fec8a5c9439fef7977a6a3640c4da8d4d7eaa0c2e3e347cf", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "work_management", "beginner", "integration", "miro"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/map_a_workflow_from_a_process_description`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `map_a_workflow_from_a_process_description_agent.py` is
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `map_a_workflow_from_a_process_description_agent.py` and embedded as the fenced Python below (sha256 f2bc882e02104c37…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `map_a_workflow_from_a_process_description_agent.py` first:

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
    "version": '2.0.0',
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
