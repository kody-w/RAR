---
name: "rar-cowork-cookbook-map-a-workflow-from-a-process-description"
description: "Turns a described process into a Miro flowchart with labeled shapes, connectors, owners, and decision points, plus a companion Miro doc narrating purpose, handoffs, and risks; call when a workflow needs diagramming."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/map_a_workflow_from_a_process_description", "rar_sha256": "8cbd2af28a5e83a207d99d37291873dc5bbe51226515f973661929d94b3b2e92", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "work_management", "beginner", "integration", "miro"]}
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
