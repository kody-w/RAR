---
name: "rar-cowork-cookbook-turn-a-document-into-a-visual-framework"
description: "Converts a named document or deck into a Miro visual \u2014 flowchart, mindmap, or framework diagram \u2014 using frames, shapes, and text; call when written content needs a presentation-ready diagram."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/turn_a_document_into_a_visual_framework", "rar_sha256": "c8f840f91737c361ba735c44560f064ae87fb50eb970b732742bd5bc3d07eb7d", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "work_management", "beginner", "integration", "miro"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/turn_a_document_into_a_visual_framework`. The original RAPP
agent is preserved byte-for-byte in `turn_a_document_into_a_visual_framework_agent.py` and in the RCI capsule.

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

Turn a document or deck into a visual framework — Converts a named document or deck into a Miro visual — flowchart, mindmap, or framework diagram — using frames, shapes, and text; call when written content needs a presentation-ready diagram.

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
  Upstream entry : https://coworkcookbook.com/recipes/turn-a-document-into-a-visual-framework
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
    "document_or_deck_name": {
      "description": "The name of the source document or deck whose key content should be converted.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `turn_a_document_into_a_visual_framework_agent.py` and embedded as the fenced Python below (sha256 c8f840f91737c361…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `turn_a_document_into_a_visual_framework_agent.py` first:

```bash
python3 turn_a_document_into_a_visual_framework_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 turn_a_document_into_a_visual_framework_agent.py   # or on stdin
python3 turn_a_document_into_a_visual_framework_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Turn a document or deck into a visual framework — Converts a named document or deck into a Miro visual — flowchart, mindmap, or framework diagram — using frames, shapes, and text; call when written content needs a presentation-ready diagram.

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
  Upstream entry : https://coworkcookbook.com/recipes/turn-a-document-into-a-visual-framework
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/turn_a_document_into_a_visual_framework',
    "version": '3.0.3',
    "display_name": 'Turn a document or deck into a visual framework',
    "description": 'Converts a named document or deck into a Miro visual — flowchart, mindmap, or framework diagram — using frames, shapes, and text; call when written content needs a presentation-ready diagram.',
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
        "upstream_slug": 'turn-a-document-into-a-visual-framework',
        "upstream_url": 'https://coworkcookbook.com/recipes/turn-a-document-into-a-visual-framework',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '102af16c21aad53c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'beginner', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'miro', 'process_roots': ['work-management'], 'process_tags': ['work-management/create-and-repurpose-content/visualize-concepts-and-frameworks'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'work-management/turn-a-document-into-a-visual-framework', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Microsoft 365 Copilot licence with access to Cowork', 'Prerequisite: Miro plugin enabled and connected to your workspace', 'Output matches: A Miro visual - flowchart, mindmap, or framework diagram - that translates the source content into a clean, presentation-ready format.'], 'confidence': 1.0, 'deliverable': 'A Miro visual - flowchart, mindmap, or framework diagram - that translates the source content into a clean, presentation-ready format.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'document_or_deck_name': 'The name of the source document or deck whose key content should be converted.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Take dense, written content and turn it into a clear visual the team can actually engage with - without spending the afternoon redrawing it by hand. A Miro visual - flowchart, mindmap, or framework diagram - that translates the source content into a clean, presentation-ready format.', 'expected_output': 'A Miro visual - flowchart, mindmap, or framework diagram - that translates the source content into a clean, presentation-ready format.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Microsoft 365 Copilot licence with access to Cowork', 'Miro plugin enabled and connected to your workspace'], 'prompt': 'Take [document or deck name] and convert the key content into a Miro visual - either a process flowchart, mindmap, or structured framework diagram depending on what fits the content best.\n\nUse frames, shapes, and text to keep it clean and presentation-ready.', 'steps': ['Open Cowork and start a new task.', 'Confirm the required plugin is turned on under **+ > Customize**: Miro plugin enabled and connected to your workspace.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'A Miro visual - flowchart, mindmap, or framework diagram - that translates the source content into a clean, presentation-ready format.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Converts a named document or deck into a Miro visual — flowchart, mindmap, or framework diagram — using frames, shapes, and text; call when written content needs a presentation-ready diagram.', 'example_request': 'Turn the Q3 Strategy Review deck into a Miro framework diagram.', 'inputs': [{'description': 'The name of the source document or deck whose key content should be converted.', 'name': 'document_or_deck_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you have a dense document or deck and want its key content turned into a clean Miro flowchart, mindmap, or framework diagram.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and start a new task.', 'Confirm the required plugin is turned on under **+ > Customize**: Miro plugin enabled and connected to your workspace.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TurnADocumentIntoAVisualFramework(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TurnADocumentIntoAVisualFramework'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'document_or_deck_name': {'description': 'The name of the source document or deck whose key content should be converted.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TurnADocumentIntoAVisualFramework().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
