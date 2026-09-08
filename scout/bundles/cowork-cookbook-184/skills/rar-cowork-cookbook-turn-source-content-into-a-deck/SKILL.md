---
name: "rar-cowork-cookbook-turn-source-content-into-a-deck"
description: "Builds a Prezi deck from source content you supply (transcript, notes, or document) with a title slide, themed section breaks, and a closing next-steps slide; call it when you need a deck drafted from existing material."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/turn_source_content_into_a_deck", "rar_sha256": "e7c77485991a900a91c4f5072f121f654c3cc0f655c09509b6a2c0a396b60e44", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "work_management", "beginner", "integration", "prezi"]}
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
