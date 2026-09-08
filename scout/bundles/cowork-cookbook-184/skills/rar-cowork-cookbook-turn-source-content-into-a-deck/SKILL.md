---
name: "rar-cowork-cookbook-turn-source-content-into-a-deck"
description: "Builds a Prezi deck from source content you supply (transcript, notes, or document) with a title slide, themed section breaks, and a closing next-steps slide; call it when you need a deck drafted from existing material."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/turn_source_content_into_a_deck", "rar_sha256": "e7c77485991a900a91c4f5072f121f654c3cc0f655c09509b6a2c0a396b60e44", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "work_management", "beginner", "integration", "prezi"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/turn_source_content_into_a_deck`. The original RAPP
agent is preserved byte-for-byte in `turn_source_content_into_a_deck_agent.py` and in the RCI capsule.

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

Turn source content into a deck — Builds a Prezi deck from source content you supply (transcript, notes, or document) with a title slide, themed section breaks, and a closing next-steps slide; call it when you need a deck drafted from existing material.

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
  Upstream entry : https://coworkcookbook.com/recipes/turn-source-content-into-a-deck
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
    "slide_count": {
      "description": "How many slides the deck should have.",
      "type": "string"
    },
    "source_content": {
      "description": "The material to build from, e.g. a meeting transcript, notes, or a document.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `turn_source_content_into_a_deck_agent.py` and embedded as the fenced Python below (sha256 e7c77485991a900a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `turn_source_content_into_a_deck_agent.py` first:

```bash
python3 turn_source_content_into_a_deck_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 turn_source_content_into_a_deck_agent.py   # or on stdin
python3 turn_source_content_into_a_deck_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Turn source content into a deck — Builds a Prezi deck from source content you supply (transcript, notes, or document) with a title slide, themed section breaks, and a closing next-steps slide; call it when you need a deck drafted from existing material.

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
  Upstream entry : https://coworkcookbook.com/recipes/turn-source-content-into-a-deck
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/turn_source_content_into_a_deck',
    "version": '3.0.3',
    "display_name": 'Turn source content into a deck',
    "description": 'Builds a Prezi deck from source content you supply (transcript, notes, or document) with a title slide, themed section breaks, and a closing next-steps slide; call it when you need a deck drafted from existing material.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'work_management', 'beginner', 'integration', 'prezi'],
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
        "upstream_slug": 'turn-source-content-into-a-deck',
        "upstream_url": 'https://coworkcookbook.com/recipes/turn-source-content-into-a-deck',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '875c4d37639b9a37',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'beginner', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'prezi', 'process_roots': ['work-management'], 'process_tags': ['work-management/create-and-repurpose-content/build-presentations-from-source-material'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'work-management/turn-source-content-into-a-deck', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Meetings'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Microsoft 365 Copilot licence with access to Cowork', 'Prerequisite: Prezi plugin enabled and connected to your account', 'Output matches: A ready-to-present Prezi deck built from your source content, structured into clear sections with visuals applied.'], 'confidence': 1.0, 'deliverable': 'A ready-to-present Prezi deck built from your source content, structured into clear sections with visuals applied.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'slide_count': 'How many slides the deck should have.', 'source_content': 'The material to build from, e.g. a meeting transcript, notes, or a document.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Get a working deck built from content you already have - without starting from a blank slide. A ready-to-present Prezi deck built from your source content, structured into clear sections with visuals applied.', 'expected_output': 'A ready-to-present Prezi deck built from your source content, structured into clear sections with visuals applied.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Microsoft 365 Copilot licence with access to Cowork', 'Prezi plugin enabled and connected to your account'], 'prompt': 'Using [Source - e.g., meeting transcript, notes, document], create a [X]-slide deck in Prezi covering the key points.\n\nStructure it with a title slide, section breaks for the main themes, and a closing slide with next steps.\n\nApply a clean visual treatment and keep the language tight - let the structure carry the story.', 'steps': ['Open Cowork and start a new task.', 'Confirm the required plugin is turned on under **+ > Customize**: Prezi plugin enabled and connected to your account.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'A ready-to-present Prezi deck built from your source content, structured into clear sections with visuals applied.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a Prezi deck from source content you supply (transcript, notes, or document) with a title slide, themed section breaks, and a closing next-steps slide; call it when you need a deck drafted from existing material.', 'example_request': 'Turn my Q3 planning meeting transcript into a 10-slide Prezi deck with sections and a next-steps slide.', 'inputs': [{'description': 'The material to build from, e.g. a meeting transcript, notes, or a document.', 'name': 'source_content'}, {'description': 'How many slides the deck should have.', 'name': 'slide_count'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you have source content and want a structured, ready-to-present Prezi deck instead of starting from a blank slide, in Microsoft 365 Copilot Cowork.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and start a new task.', 'Confirm the required plugin is turned on under **+ > Customize**: Prezi plugin enabled and connected to your account.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TurnSourceContentIntoADeck(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TurnSourceContentIntoADeck'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'slide_count': {'description': 'How many slides the deck should have.', 'type': 'string'}, 'source_content': {'description': 'The material to build from, e.g. a meeting transcript, notes, or a document.', 'type': 'string'}},
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
    print(TurnSourceContentIntoADeck().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
