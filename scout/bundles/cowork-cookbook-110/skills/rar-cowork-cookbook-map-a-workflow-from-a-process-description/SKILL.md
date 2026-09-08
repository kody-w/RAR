---
name: "rar-cowork-cookbook-map-a-workflow-from-a-process-description"
description: "Turns a described process into a Miro flowchart with labeled shapes, connectors, owners, and decision points, plus a companion Miro doc narrating purpose, handoffs, and risks; call when a workflow needs diagramming."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/map_a_workflow_from_a_process_description", "rar_sha256": "8cbd2af28a5e83a207d99d37291873dc5bbe51226515f973661929d94b3b2e92", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "work_management", "beginner", "integration", "miro"]}
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

Map a workflow from a process description — Turns a described process into a Miro flowchart with labeled shapes, connectors, owners, and decision points, plus a companion Miro doc narrating purpose, handoffs, and risks; call when a workflow needs diagramming.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

This entry carries the upstream recipe itself, under its licence and with
attribution: the prompt verbatim, the prerequisites, the step-by-step and
the expected output. Toasting made it deterministic — the same call returns
the same recipe every time — and callable from any Brainstem. The upstream
library remains the authority for the recipe and links home for the source.

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
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "open_questions": {
      "description": "Any unresolved questions or purpose notes to include in the header frame.",
      "type": "string"
    },
    "operation": {
      "description": "What to do: run, prompt, plan, checklist, describe.",
      "enum": [
        "run",
        "prompt",
        "plan",
        "checklist",
        "describe"
      ],
      "type": "string"
    },
    "process_name": {
      "description": "The name of the process or workflow to map.",
      "type": "string"
    },
    "source_material": {
      "description": "The document, meeting notes, or description containing the steps, decision points, and owners.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `map_a_workflow_from_a_process_description_agent.py` and embedded as the fenced Python below (sha256 8cbd2af28a5e83a2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `map_a_workflow_from_a_process_description_agent.py` first:

```bash
python3 map_a_workflow_from_a_process_description_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 map_a_workflow_from_a_process_description_agent.py   # or on stdin
python3 map_a_workflow_from_a_process_description_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Map a workflow from a process description — Turns a described process into a Miro flowchart with labeled shapes, connectors, owners, and decision points, plus a companion Miro doc narrating purpose, handoffs, and risks; call when a workflow needs diagramming.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

This entry carries the upstream recipe itself, under its licence and with
attribution: the prompt verbatim, the prerequisites, the step-by-step and
the expected output. Toasting made it deterministic — the same call returns
the same recipe every time — and callable from any Brainstem. The upstream
library remains the authority for the recipe and links home for the source.

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
    "version": '3.0.3',
    "display_name": 'Map a workflow from a process description',
    "description": 'Turns a described process into a Miro flowchart with labeled shapes, connectors, owners, and decision points, plus a companion Miro doc narrating purpose, handoffs, and risks; call when a workflow needs diagramming.',
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
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '242b2707d11ad45c',
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


# The toasted capability, generated by @kody-w/skill_toaster_agent. A licensed
# recipe entry carries the upstream recipe verbatim (with attribution) in
# _SPEC["recipe"]; a metadata-only entry carries RAR's own method for that shape
# of work. See the module docstring for which this is.
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Microsoft 365 Copilot licence with access to Cowork', 'Prerequisite: Miro plugin enabled and connected to your workspace', 'Output matches: A clear Miro flowchart of the process, paired with a narrative doc that captures purpose, ownership, handoffs, and risks - turning tribal knowledge into an artifact the team can act on.'], 'confidence': 1.0, 'deliverable': 'A clear Miro flowchart of the process, paired with a narrative doc that captures purpose, ownership, handoffs, and risks - turning tribal knowledge into an artifact the team can act on.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'open_questions': 'Any unresolved questions or purpose notes to include in the header frame.', 'process_name': 'The name of the process or workflow to map.', 'source_material': 'The document, meeting notes, or description containing the steps, decision points, and owners.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Make a workflow shareable, reviewable, and improvable - without spending hours building the diagram by hand. A clear Miro flowchart of the process, paired with a narrative doc that captures purpose, ownership, handoffs, and risks - turning tribal knowledge into an artifact the team can act on.', 'expected_output': 'A clear Miro flowchart of the process, paired with a narrative doc that captures purpose, ownership, handoffs, and risks - turning tribal knowledge into an artifact the team can act on.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Microsoft 365 Copilot licence with access to Cowork', 'Miro plugin enabled and connected to your workspace'], 'prompt': "Map the [process or workflow name] as a Miro flowchart.\n\nPull the steps, decision points, and owners from [document, meeting notes, or my description].\n\nUse Miro's diagramming layout with clearly labeled shapes and connectors. Add a frame at the top with the workflow name, purpose, and any open questions.\n\nThen create a Miro doc next to the flowchart summarizing the workflow narrative - what it does, who it serves, where the handoffs happen, and any risks or bottlenecks worth flagging.", 'steps': ['Open Cowork and start a new task.', 'Confirm the required plugin is turned on under **+ > Customize**: Miro plugin enabled and connected to your workspace.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'A clear Miro flowchart of the process, paired with a narrative doc that captures purpose, ownership, handoffs, and risks - turning tribal knowledge into an artifact the team can act on.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Turns a described process into a Miro flowchart with labeled shapes, connectors, owners, and decision points, plus a companion Miro doc narrating purpose, handoffs, and risks; call when a workflow needs diagramming.', 'example_request': 'Map our vendor onboarding process as a Miro flowchart from these meeting notes, plus a summary doc.', 'inputs': [{'description': 'The name of the process or workflow to map.', 'name': 'process_name'}, {'description': 'The document, meeting notes, or description containing the steps, decision points, and owners.', 'name': 'source_material'}, {'description': 'Any unresolved questions or purpose notes to include in the header frame.', 'name': 'open_questions'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you have a process described in a document, meeting notes, or your own words and want it mapped as a shareable Miro flowchart plus narrative doc.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and start a new task.', 'Confirm the required plugin is turned on under **+ > Customize**: Miro plugin enabled and connected to your workspace.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class MapAWorkflowFromAProcessDescription(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'MapAWorkflowFromAProcessDescription'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'open_questions': {'description': 'Any unresolved questions or purpose notes to include in the header frame.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'process_name': {'description': 'The name of the process or workflow to map.', 'type': 'string'}, 'source_material': {'description': 'The document, meeting notes, or description containing the steps, decision points, and owners.', 'type': 'string'}},
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

    # ── recipe entries: the upstream recipe, verbatim, deterministic ─────

    def _recipe_context(self, kwargs):
        extras = []
        subject = self._subject(kwargs)
        if subject:
            extras.append(f"subject: {subject}")
        for key in _SPEC["params"]:
            value = str(kwargs.get(key) or "").strip()
            if value:
                extras.append(f"{key}: {value}")
        return extras

    def _recipe_prompt(self, kwargs):
        r = _SPEC["recipe"]
        lines = [r["prompt"]]
        extras = self._recipe_context(kwargs)
        if extras:
            lines += ["", "Context supplied by the caller:"] + [f"- {e}" for e in extras]
        return lines

    def _recipe_attribution(self):
        src = __manifest__["source"]
        r = _SPEC["recipe"]
        who = ", ".join(r.get("authors") or []) or __manifest__["author"]
        return [
            f"Recipe: {__manifest__['display_name']} — by {who}, {src['source_name']} "
            f"({src['license']}). Source: {src['upstream_url']}",
        ]

    def _perform_recipe(self, op, kwargs):
        r = _SPEC["recipe"]
        ref = _SPEC.get("refinement") or {}
        if op == "prompt":
            return "\n".join(self._recipe_prompt(kwargs) + [""] + self._recipe_attribution())
        if op == "plan":
            lines = [f"Steps for {__manifest__['display_name']} on {r['platform']}:"]
            lines += [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "checklist":
            lines = ["Before you run it:"] + [f"  [ ] {p}" for p in r["prerequisites"]]
            if r.get("expected_output"):
                lines += ["", "Done when:", f"  [ ] {r['expected_output']}"]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "describe":
            lines = self._provenance()
            if ref.get("when_to_use"):
                lines += ["", f"When to use: {ref['when_to_use']}"]
            if ref.get("example_request"):
                lines += [f"Ask for it like: {ref['example_request']}"]
            if ref.get("inputs"):
                lines += ["", "It will ask you for:"] + [f"  - {i['name']}: {i['description']}" for i in ref["inputs"]]
            if r.get("business_value"):
                lines += ["", f"Why it matters: {r['business_value']}"]
            return "\n".join(lines)
        if op == "run":
            lines = [f"{__manifest__['display_name']} — run on {r['platform']}", ""]
            if r.get("what_it_does"):
                lines += [r["what_it_does"], ""]
            lines += [f"Prompt (paste into {r['platform']}):", ""] + self._recipe_prompt(kwargs) + [""]
            lines += ["Procedure:"] + [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)] + [""]
            lines += ["Acceptance checks:"] + [f"  [ ] {c}" for c in _SPEC["checks"]] + [""]
            lines += [f"Deliverable: {_SPEC['deliverable']}", ""]
            if r.get("tenant_caveat"):
                lines += [f"Verified upstream: {r['tenant_caveat']}", ""]
            return "\n".join(lines + self._recipe_attribution())
        return (
            f"Unknown operation {op!r}. Valid operations: "
            + ", ".join(_SPEC["operations"])
        )

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

        if _SPEC.get("recipe"):
            return self._perform_recipe(op, kwargs)

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
