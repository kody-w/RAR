---
name: "rar-cowork-cookbook-turn-source-content-into-campaign-storytelling"
description: "Builds a Prezi storytelling deck in Microsoft 365 Copilot Cowork from a transcript, research notes, or campaign brief, then deepens a chosen slide and adds a talk track. Call when turning source content into a deck."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/turn_source_content_into_campaign_storytelling", "rar_sha256": "ec8a3513294f9ce838dab1917e1b39510ca12783643c071b9fc6f7f58b40d88a", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "concept_to_market", "beginner", "integration", "prezi"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/turn_source_content_into_campaign_storytelling`. The original RAPP
agent is preserved byte-for-byte in `turn_source_content_into_campaign_storytelling_agent.py` and in the RCI capsule.

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

Turn source content into a campaign storytelling deck — Builds a Prezi storytelling deck in Microsoft 365 Copilot Cowork from a transcript, research notes, or campaign brief, then deepens a chosen slide and adds a talk track. Call when turning source content into a deck.

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
  Upstream entry : https://coworkcookbook.com/recipes/turn-source-content-into-campaign-storytelling
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
    "depth_topic": {
      "description": "The topic, proof point, or data point to add depth on in that slide.",
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
    "slide_to_expand": {
      "description": "Which slide number to edit for added depth.",
      "type": "string"
    },
    "source_content": {
      "description": "The meeting transcript, research notes, or campaign brief to build the deck from.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `turn_source_content_into_campaign_storytelling_agent.py` and embedded as the fenced Python below (sha256 ec8a3513294f9ce8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `turn_source_content_into_campaign_storytelling_agent.py` first:

```bash
python3 turn_source_content_into_campaign_storytelling_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 turn_source_content_into_campaign_storytelling_agent.py   # or on stdin
python3 turn_source_content_into_campaign_storytelling_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Turn source content into a campaign storytelling deck — Builds a Prezi storytelling deck in Microsoft 365 Copilot Cowork from a transcript, research notes, or campaign brief, then deepens a chosen slide and adds a talk track. Call when turning source content into a deck.

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
  Upstream entry : https://coworkcookbook.com/recipes/turn-source-content-into-campaign-storytelling
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/turn_source_content_into_campaign_storytelling',
    "version": '3.0.3',
    "display_name": 'Turn source content into a campaign storytelling deck',
    "description": 'Builds a Prezi storytelling deck in Microsoft 365 Copilot Cowork from a transcript, research notes, or campaign brief, then deepens a chosen slide and adds a talk track. Call when turning source content into a deck.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'concept_to_market', 'beginner', 'integration', 'prezi'],
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
        "upstream_slug": 'turn-source-content-into-campaign-storytelling',
        "upstream_url": 'https://coworkcookbook.com/recipes/turn-source-content-into-campaign-storytelling',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd8d6a2c4dfe62de5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'beginner', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'prezi', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/prepare-marketing-campaigns/create-marketing-material'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/turn-source-content-into-campaign-storytelling', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Meetings'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Microsoft 365 Copilot licence with access to Cowork', 'Prerequisite: Prezi plugin enabled and connected to your account'], 'confidence': 1.0, 'deliverable': "The recipe's output, produced on the target platform.", 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'depth_topic': 'The topic, proof point, or data point to add depth on in that slide.', 'slide_count': 'How many slides the deck should have.', 'slide_to_expand': 'Which slide number to edit for added depth.', 'source_content': 'The meeting transcript, research notes, or campaign brief to build the deck from.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Move from raw inputs - a research debrief transcript, customer interview, or campaign brief - to a polished storytelling deck, with iteration built into the flow instead of bolted on after.', 'expected_output': '', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Microsoft 365 Copilot licence with access to Cowork', 'Prezi plugin enabled and connected to your account'], 'prompt': 'Using [meeting transcript / research notes / campaign brief], create a [X]-slide Prezi deck covering the key points. Structure it with a title slide, section breaks for the main themes, and a closing slide with next steps.\n\nApply a clean visual treatment and keep the language tight - let the structure carry the story. Once the deck is built, edit slide [X] to add depth on [topic / proof point / data point].\n\nThen add a talk track across the deck so I can walk it through confidently.', 'steps': ['Open Cowork and start a new task.', 'Confirm the required plugin is turned on under **+ > Customize**: Prezi plugin enabled and connected to your account.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': ''}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a Prezi storytelling deck in Microsoft 365 Copilot Cowork from a transcript, research notes, or campaign brief, then deepens a chosen slide and adds a talk track. Call when turning source content into a deck.', 'example_request': "Turn my customer interview transcript into a 10-slide Prezi deck, add depth on slide 4's ROI data, and give me a talk track.", 'inputs': [{'description': 'The meeting transcript, research notes, or campaign brief to build the deck from.', 'name': 'source_content'}, {'description': 'How many slides the deck should have.', 'name': 'slide_count'}, {'description': 'Which slide number to edit for added depth.', 'name': 'slide_to_expand'}, {'description': 'The topic, proof point, or data point to add depth on in that slide.', 'name': 'depth_topic'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you have raw source content (meeting transcript, research notes, or campaign brief) and need a structured Prezi deck with a talk track in Cowork.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and start a new task.', 'Confirm the required plugin is turned on under **+ > Customize**: Prezi plugin enabled and connected to your account.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TurnSourceContentIntoCampaignStorytelling(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TurnSourceContentIntoCampaignStorytelling'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'depth_topic': {'description': 'The topic, proof point, or data point to add depth on in that slide.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'slide_count': {'description': 'How many slides the deck should have.', 'type': 'string'}, 'slide_to_expand': {'description': 'Which slide number to edit for added depth.', 'type': 'string'}, 'source_content': {'description': 'The meeting transcript, research notes, or campaign brief to build the deck from.', 'type': 'string'}},
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
    print(TurnSourceContentIntoCampaignStorytelling().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
