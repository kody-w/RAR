---
name: "rar-cowork-cookbook-turn-source-content-into-campaign-storytelling"
description: "Builds a Prezi storytelling deck in Microsoft 365 Copilot Cowork from a transcript, research notes, or campaign brief, then deepens a chosen slide and adds a talk track. Call when turning source content into a deck."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/turn_source_content_into_campaign_storytelling", "rar_sha256": "ec8a3513294f9ce838dab1917e1b39510ca12783643c071b9fc6f7f58b40d88a", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "concept_to_market", "beginner", "integration", "prezi"]}
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/916adeb1pbmX1G/9SFJybYAgQSudddqQAgQiEESIIjvcpjneRAolf/eB0kecq9vdae6P7XsRALOnvd+9j4+/P5m911UNm8f386+XSxYO8viyG8WduEt6PJWNin4KlMH/Ldwy6JrYqfvyqZ9e/fm+a3bxFUXlwUgp/o489qFvVAa/x4vWrBo6nzArQgXnu+mi7hYHGO3Kdsy6BbrDQb4VnFWdl/EBE2ZA/KusYsn33eLxm99u3GjRVF2fvtuUTYL184rOw6LhdPEfvBu0UV+Afj7lV/Mwt2obMGNNos9/2GD7T2U6uwsnVm76YcFDWxc3Ga6rm+KWb+27BvXf9jnFx3QtCsBzaz1B2CnPwKZmd++ffz17+/eYvD77ePvb25mt+DW2wXwOD/o6Sc5D6jpl5bn77wAOGU2+Pr4Vk3A5QW4rvwmKJsc3PL8YPG6+rn1M2DYv/97erObsP3l46di8fp8epv/nPpiNnvRlXbb+R5wSWU7cRZ304cFmd3sqQWOm02bDW9BxIrww5PyG6eyWvxtfvbzU8iH0O9+/vRWAhXsOZ6f3n6Znf3prenn3x9mLtXPv3zIypvf/PzLNz5t7yS+283MgNYfPr+uX2zBwm9L42Dx+aww9EtW47tx5QPm39k3f56qv9i9XPL5ufjnsnq3+DHn2Z6/AX2fOekAvj9mC3wAKN8+JGVc/PyS0ZSDX9iF6//8y79i60YgF7K47f6P+P76ZBz5tge89XLJL+8e4fv7Yvmy7SvPfy22AgnzVywBy7+I++qof8X7Edl/YA3S1G+/xvKH7H5EsPzb4td/adt/RfBuEXx62/lZPIC8czL/4+L3R4r8+pP37eZPf/8DsP7fsnnW4Mzhc24XceC33efPv/70LO2f/v7rT30Fsti38899k/2I54/8+pDzJw++Vv38Z1ogXyvSorwVi681tPi9rP5H88eHhW4DNPp2v/24+L4S589yMRvxRejTBd9VYwt0/c6Pv7z9AWCoANb07uMxwI9/+7fvwPXsln23AAHu4tyflb9EcbsAf2fUaHzg1zYGjn2tA/k/R3jWuAwWv/1P9wHH790X6q9mez8/3fj5hZCfZ4T8/AWKP3+P9b99WFyAlLKJw7iws8WJVJRPhR0+cLUFwgCkNwNALQdQvAfF/X7+MTeH3/6aoM8Pnh+q6bcHzsdPTDzR/IyHbZ/5H2bLjRnmn3a6oL35o+/2QFxWukC3IM7mrgJUKrMB4OnspTaNQXfwYoA4s7AHb+DJjzOz3377zbHb6FPxBPD14tmn2hVY8FWdxfv3wMggi8Oo+1T4oCEtfvr9j58W/7n4r6gezGcZCugqrzgBDQ9nWVqAuutzsAyEEAQdgMojTr//8XI1YFOAhg2iGgex/yQGDkp974vfzxz5HsE2C8cH/ga+zquy6ea+F3cfFnyw+KovEDo/mvsG6KMd6ICgrXp+4U6Aqw3M+epJ0JAXLUjONpjeLfrWf0j9zWnsh4o5AAC7+21xpBXQpcoM/G9W87EIEJdFDNz/NSue9wGT5qd2QX1h8WEhzZm6qOzGrqLGfskI7GdcQHf6Qv5o1oV/+1TMvdmfXfUom6d7wCLgGfcV0vdzzEGjzwFGeO0X2Y819txLL4+e2nwq2ldJ2M0cChe0CCA07GNvbhT/8UqpNir7zHv4D2g6c3pFwXtF5ZGDl0c/++GI8XWa+edx6VOPQDC6+P90rJr9QrLsiWHJC7NbMNLlZD7j9WX1cy4FQ80CJO2zNr8NOl/A7AumfyqyGCRfM/3Hc+Ujyq81T5zsGxCUE3l68AcpBuI1831UwJzRTTPXjv2p+NI83gFVH0gJkgDABSinOYu/CJyfftE0ApgwX38bJB4Z03izp0CWL6reyUAGBr7vOcBVQKtmruJXhEE5+HNF36IYhOR7qxaAO8g6wH8BlIhBXYIG8+EroD+fflH9T4TPeWkmecySPSji5sEA6OHPCs4xvMUdwDK7e870wM6PDybAjLzqZtsdUEb5u9dNv/HrPm7jR8Y8/epXALzfz99PS+e7/liBygHOAvVR9cC7j4qasyEH0xDQAcQfFFgeF2A6AE55OeHB0M5neABZ9Bpfnxwft18G+Y8ynNvaF8LZkJlmnhReuV5M36PI5UdpAvjl84qH3H/MtK/SZt4zkrYADYHEL0+faf3hORU8x47FF74f/2nT9PNf21c9+rz25wT4uIi6rmo/rlbP3vylNX8AOLZ66to+2vT7p2rvX5n5fq64919K+/332PEnKU8HfFz8NU3/xOJVKR8X8AfoAzQ/El+Z9voAx9DvKfM9Oj/9VJz8b5gLxJc5SLU5jBOYC742yC9LQJcMGz+cFz8bZjv32RlqHh0CxORT8X3qz6UHGlARzqnalt9BwmNSAGXwBZlejQw8Kjog25tnztCfN32PQmn9t49Fn2Xv3gqQhH9xszc3rnzO9XbeLoKqAuNcF/uPq0eAxm7++eddtPz4YWcfFjsfwFTWfp+Pr3Yzt9vvyuZpMDDUBRLeLTzgpnaGdGDwLHwuObsFOQzSdzasm6rZkue+cJ4kQZPvos8d6BruP+tzeewzwaN3My4AlKrAhNo9WgYQZD8vZ2AEDWHx4PSAquIxLzz7xQ+Ffp1t/1mkMVMCjl75ce6i716ABL7BfuTd4uvWApj62uw9NulFD/bRv87bmtn3D5L5B6ABX1+Jvv6zheO//f0Hej00BtMnmJ3/WTOuvAEUA/DyWPUMzaMHvwIT2cOPrX1yBZMsQEeQgj+yecb+Z3sFhjhzVpcL3wOxm1EHONd/uffH/P80NP84irnvP2D4Lw0CsxbOPIF8s3XG2B8oAbR4NAjQZucwfIvvNy+Xj53krC+ISvf8h4/f30CJ2HMqvYrktRUBywGevm/nMWsFMAUIBNfP6gfP/i83KS9ubWSDsRiw813cXmPwGiHQgHB9fI17tgMT8NaHnTWBwZBrw8gWX2/QtQttYYcI3E2wDTDcQSEPx+2370KQ5/GsIUZsA4ggkACFEQiEL0BQz8M3+MbFtghkE46NORhhO99I03jOjIfZTzNnn37dL83ueVn/+5uzQed0RFuefH7o1RIGN7fOqXKWzcYvsWBSkYoz75Em+heEX1/ZiWrtgxl4R6kPeTo1jANjalOwOzsakoTXnPfdA5YOa1nWdS21xU0G8vGYxUliOXydycV90LbVpiTuY+/CkFFP9a1X6zUtCvNVijYXXq93OxNLWfzWt7WwtvVLxaNXO+OjcYCT7Yq4OkiLTmp99LGuDHCbuE2CttLyXdm394OtL4ezeCd0K2u9g95za123WlgU+a6K/L22t6PUcHVE0jd7njs5kWHrTuXW02S2q31ZJjD4XXcaRl2X7qZyrztPd2LVKphUtyi2TkOztmteStXNdZfU22N49lT9bvc3YykMAa4w3QU3ByXJ87U/DEU2rvqyIcAkhK/d1VKu8OGEO7CkbYTloa4wJ2yyhjvoyTGEDBfaSTiJyvW97WvouEfS41nk4wi5I5fwmG4gzuQpT42WnnDxh2vCYfwRhVXjkpy7YLAxsj/SeWutKSlNkuqMRmVKeZtaOLawmhlOQjki1WcbeZ21BKwJ28qHsTS7l5KWT2uI3Rsn+pyR1vYaT6oM62Jjk0w1Gxjv47ttWXV2hqI2imtX8RNVLEzGgPZUzwvDBjvH8uR6cTCIx2Vn6yF2T3QJIjPIEPyTWIQbQ9oxbF70Qr01wg1dx0V00okkzNicXCGwD9nmVT3pw7i0I3FQB0+/sw5txhcMVvZNe1j5ZgelCsF7XkSd95lnXa+MXGH7StUNl0RiPgw24v08XizZvN9kH+SpKEU0iqhIdLYdQQ0kbXvUd6aF0OFYFekFh1ZRSKqIaNrulnAE8txyqp5OpT0aYWdr1MBerk1V6/HuDEYLufZMR9/u29EE3aAOvPhuOTW8a0zDsrr9EA+nnoBToRpu+yUe9fTBLFw+VyFRiQeBIXa4Cw+JtjX6upncotqwyo6B8NXthmCoUC616myUccAgR1bb8t3ZMaLJ61OOvKYurMCugnp0alZYXCcrpFhlMr605FFUjoqa5M6gjBEeZf6u21aZaTeUoVrGrnFuzYH37z2M0Pnh5BsVd+EVve7oBglvSn5QKms1yIdJ3VlkT9UbL0X9/WaivNRgjdxX0I5CJv/U4WF0Ol0qHc10y5TLinJCQ/LDRAxXhdsPI95Um2Zz23e3eNhJ2p3Np3qglQOo48k128A3pE3R7mmcu6KVUVWm5OxrrBFvayHKL3VtGcT1ePW04+6SJrogooJ72dRXyB8Nw6fEHrv62Olsq1GVXmOr3q+g7Sn2pt64RB2RC2tnqRs3IeG2ZhQXmoo0CMQ2tBmIqB5K+7Vx4PYCKLCLxIirKldP6rI6RelNJ0h5r2KE5i47nB01546gOpCZ1iROY9eWQ3de7uo71mVPFt0fecGo95JMHp19saxIvN7jU2MMe5aJWcRDy9S7CYwjV0VDHETkmLct6QkKKl55bnVxl5jQrjj1lHFM2fS+VV6XpOfFEFb3QcPo3NGZ+mVY9NTgNngoutzZjGU5vGt657LGwYFkHkL7S2lGeNIeDynZ4qI0kd7IF+r1QEdaVB9BXVlL16IQVSSHXdzW4nTg1tHy2p02A0cU150gn/ZkV42QnzRHGd6yWlHt4dTbkcZGQGS8ECwYzQmzyZXzpBGYsMlRhcPMtT9aIz+qBcm5qlmOZww53VUcw8rx2KMXqCVp+4Ro/aAmtaUeUzUMYs/qBw5jyowdgpEyTwwsdB5l+hJHUqcdw7gYI3tMyByN1s0J/7ru6TGEWKbk4n0aV8a+SiUapdcojx9OxwqVELYdoVYYDxeqMZkrzacxiWVTVYeQFkLtuV3eRqRI7UMWaaq205EBR8tEv1JNwbRrSDZbQaCw0pexzDMHfXMbI5aFMO0A9tOFaLbo9Xyx0Opyg+Q8uFZLYjk4hICWeOSi9y2l2ME46mXG7LktDyEjpm5EjheEmNbug7/aZsxS7MatQHoWHoflsDwOYbikL0sxG2rxMolE7zDNEc+aMLkoqz09UmfuqDqmtsN3Egztz3ZCWqPbZZxkHsr+DDC/vdRCPN4vKZrX1UB6u9HKumu5F+XY6DmdRAPQbczY68/kFHp3vj3mUXdeJmRlkvxwnLIQK6dElI6rLaVC7hjDS7VaOeIEKbwOhzRX7E1SZ0n8fIhRVnKCKhyj9lgdMH0JT6J5dwpJR30K0zbLvUZcdxCkkFQZG6meb+ODsPeuIbET6MLZJake2nlrDLt8jVjXvoid8GRJfi1hl43GT22DmoW9azaCnyrHMN2fVFg7oSx1pdqGNwjS70mTdoR0hzpedtVhjSLp3a0Kyo3YVjWTijBa+CtYCJFaNE0GVUeMMuEwPTE+mcTCoGt45C2bzqKq08EzDA/U8nnH70+xgjcJDNHBptGFMCklGDX926iJVYddvdOp2HRnOs0UWElPZmh1om7ENSJ0cFbQeCh0IanJh9stjzAO1nuUyhiesjWGSiGrJbQ7vLOFjWtIjNpfqY7Jy0S8mUR3Y1a32F2HOEOeBBfXUTrkOZNTNxGaI96+0rfncgwgSyBXKZNXEpxph1XjNEq5UfFxq5/U8mzFZ4HlV6ZXMxETDvBp5OXQOnJQNp7v2aYRLZ71z9fDqh8JfskudypAemzJORuIuXNk0J7zkYvaXkLX3NGqr3geekM2pZCxnTytotdhf7sNVlcTvkDJIY/Rd8ufPOnaX06MzU3nTlaNYrnqkaa9dUpU9HcLpifrOp2rc9QieRsOoIM5Gp3AWZbSWW0eDoesSVlVDldqhRK1tpNEg7DFuOHVhuLkKs4R2WXy7W1p0lOtReEF6lQoPRTpGYuv+CHlusaSyAryBdrrzZRBuD2l6f3Nd9g+hmMtHvmMoVigRaKN/Wm8FxV/t+SbWvGhc0+LWOzw3mRofKSXFB1rZKGT4Zky+SsGQUkoXFjfglSSVs92agfF0cSc5DxGljRmeS9OSKFM8rozQxoku9nTZ5FJKb9I8zw6uOb+5JAwqYvnPVRA8marhe3per2ltVu0ukqasLrjYpuQBMZVpZFi6XLLCgIrnUjVdnde29aqe8kO/dmTS5Fe53DUF7mrJWLsFQm9xO2q2l8U2TwnDcIM2KHVbLIq2t6rvbO5l/ThcjBXd+068coQgDKztbJnC7z1e7GEZDjksiWK75mSBN2tuAeIL2qEcNtefLEODymdeubZS3OWYljYZtR6qLtisM+JhRmHTNhAiQUFlKi6aLBO1CqTtOxkm+WQ6XmbbRx+YKYz2yBp4pfBdHL3LaNHpJsIhMYk3Xjbs8UuPMq9xcA1xu4L0L/bZlWZRUNNJR2YCFXT8jkpx+UhcWl51IlNJFhYleNtymOoOpkCb7bH+DyByjifrqJmJalPuAp/QSx2cjlTXPv7oU6pap1sam7EFClQxZ0JCRSujbdl759PnDTa9J6/5dDlZspIx+z5IxWmwcCsWjQ16+uOwaJDTu0NXojPW+gyjNxEy8TW9C4qCuZiSb/SXHsM16gIR8XWpJe9MDBYSREXY3UwxUJVHefok/4kSyDOlynVlP3qwhHH61LFAGBIB1nGk2NrE6qVFUYjildbRYzYw288r21am1XvbiOZ+p0syKqDSYw4T0ecCK/idpNEF60nw4k6DJrBjRrCH6BdLbKU6tq0ZBwkJUaS+/GODRvXD10IMiBOtVzGrEYyDfcB49abMmFGXB9Twqg75zgNabVmqJEXWWJcy2roDMervu/5TUVy1dVgM7dVdnck3KgHkdHzTXqSHJs+qNSO79bng0JMlqzA1Epnna5e7QMCO2aJG2nD6uCQkdSfMXQ3puv72BF7ZX/che6Zq7ia0etTGrTMBTtDSOhA+5jPdsK+5VJa1W8MXWHR1bfDMmxJR3c0g9zvefZGlAYLG+lEcvYxpzuDUcvsaGyw4/LC7ur4XqQhei5UmzL1asrKWNVQjkft413XcxOnIcbopgmxfBoYeMmHnkCFOxOrI4wESmOHim6zfW+qFELsLnv2TsUtTm65I71ey+F4ThJhd4TKa3+Iqbu0h28aaayN1MJSX4dlJcKRZuufFXvDXVoJWsor9ygYtyTVLsrZ3cLTuEvgQUJgWMELZledOQj35B29i/p+O+Gr8G5uOnjdEAUo47oLj6xaEq2Di+H93OantaKTTLDCO34L10wYohGkkXaLGcrKzwU72hh0rJS8Qu2qri0GHmaCTXG7NlswLdjNLarAjFseJN+Z+N1BRkktvjp2sz+caNVgDDlMclbmav268TdZ3gqNT2wbjJUdO/Cwg2iNF5jyaKOizITE+e294lrZ6Y/700ZZXSYZxxPrAqZDn3cslKERGdOKEwy2kJJbMzIckF6cVLWvRaswBdM4aYARMF+eIhU/jg62TlOxXEPFbasWyhHfiUZuJIcWCe8Fpw/tLmG2u6n3k6lDl7GkrF2u9W/r9i6fbq6Ndm6HlTnRTnfDuLpBB8bm9UXRzytbRAIvt5HdBMZJDIbXXBdIngDyDZSN5C8rCdpzPVU0yNgGSUxdYE3LRoTqiSukntarxu7uiGZfxlvEVld7t7IqlrCWRl557Ho7uBBnnBMwti0VCQ2yiWRLepocFWuRRMUolg/bC4KoHsCgZpBwJdQCC2Q7WqCdmm8dbN+3S3FF9TokO0XlqrVTBVHa79h9M7jYEVkhjH1hcYk9rNFKZcBWG/L11AT7ytUq2a5XoK8mzWE6r9PNchWPaMEdatkchksuxJFRnWTQic8lpe4Cdp3lIk3340hflTRy0svypK5775rYxfV4SgQWSkcOOnIoqD+jCHAIw6HcXcp5JsWYO7nrOjSbrDkYOFeYfncSFYPU6ANiBdGaZeXjFI6HHEeHAmw/Dac2ikYvdHXbT8xuOkmavV5Bfd/2yqU/pMttS8VbCkIwN0onRomtaqBrmolG767UqXNvSihfwVYn9z2bmPjSryGPjTA2IWRhDTubNkBMU7mTinssD6nKN+nNlYbhIPdb9ozzoFHUBtIRatiUvplOJqgigoWhQGw1IZzudUNCVIsiGHvaBmteiIiINfHjihnzyxaxlmkEIoZkTcMkesXnezU/IP6OJ0QPcqKSWvMSeR/jfE+s0E1VqX3NOBPBEBrk37BUdtMLs6eGI+/4VWLhiknruMlAqYvgWITKoOszwwAmBFZdNliyul4qjACO65eBTPGc7Z8KYZt6+eo8KfomPmgYeXSnXYlvcmkVmZ4J730n8M6x44ldCJXTCt9vGI91OAJuMvsYnNamYdf+oE67DLoyI+s3smVjF+li8zt0XzNHAUfw3fEasDaHJVU5Lc8byViVfIoIsqCI95C6h7frcEkaehM3t1UaQ8c1VxU+PAiDVCHbywlRttruOGKFkSerS6YfcQbr8/o+UIG0qqetqGmyim8PYuknMWZH0kRs79KN5enK2lDbCZbSUeR3OBTglsApGrNLMda7RwLvx36JbAj0WIX5eW8TyW70aCw2DYmDxmaN9Z7UKa4Ns+t7I11N/cop/QVDPbXHRszj+dpaBmLoJ1Wg2obBJtrlvN1IQu3fQMy0Lrj6awE7ewRxlbKAWloTu4xGaNtH6811n4QFaJxmOfkQW1zKsBKQbVnez9ewk7G1NDa66Z5KdN/cawaxa69arwsEEbPDuim2wenEIWbb7KDVtC8588BqJ0MDzg3XzdocGwpnS+wgO56/FAVlC7s8c2qlkz8uT45Gnar1XUN3R3EfnT1NOJqBqpaeF6D1TSLD07YiVN9iYTyCIf8cTycIRdNkc5xum2yC/MzqeoYodLlVnMAh2wNdOyVydNJVdvVH/R6usnBHQIxAuUm1rOUTE3u0m/TsMKrlNizGaJPzY5Y5jaQuB05aQ9Rxi05I404DDZXKqWvYbSPioWNdw8MJEybR5Qif3wvEcJUGwW2daUwbR8qtpjgRlxI7G7dTsz4ep1NwzVqrhqmmzd1CUbsdee8JK0VQ4rIODrl2VzS5M4yqj9GeiINW4G9ufpr2w22LOKoSoGBTtj0ZIh9AKHm5qHgVasMhOCMbbRfaQm4vD57NppHCS+tdUshrlVnjVawnBgE7cQZtlrkvKEd9ddaMQsOOuA1bXCEO1yImk2BpHBupa6ZjzCC8nO62PKeQh9Tc35eFuF5VgU+sRzvfMwqzRSUh8jsc63eO04mehioOTPQbByqlmyOgCpsbNraliqJJC37jkyswjVriPs3ou24jx+neslQ+nYrbKAkAfs5Ev0ewfDATaQfdbc8k7OswCPcVxAyTdHBYxhaYKXe4sxdDyroT06WPHhzOJCgCCk3sYHOMGTKbEbqE1+EWNC2JSnR3c6RdW2+94XC9FBknU3CH49092iBqXXBXr0n8kLsdPafso43O4KKQ+K0rDPUmGg7bLTR0TWAT47XwsWy8DxC8rTLXcocVfnWHPFGHMbotNxa7RQ8curQIsrYtRW4Mr0/zyhdKW6+bzXRfJTdhs4R6dZS4pRxMbXK9unZn8sFuZeZL+LpN7B5zN10hXnEnagyqxC1ecdJJZY5H3Nd0n9Dt/ZI4Cxv6ahQrax/IazlDMw2tRDUVVGktjPdMSsmav2XShVLSw+qUkykh9sJ87CH5dKTe3Mu6jAqwt3W0Xa1KHLWylIk57Sqr93y39W6QyhKr1mplXOyW64CIV0YIsRLu4ksUmtZ9dU3x2hvpjRFL8La/3gyowu/oySnMJrJt3jY8UjB9tsXlDVZsMQLGEyVc89wlFiEYh1R4CU2X2Luj6/PyiMOnlb8auV2MrBPQRjNXUbwUF3HCYZ0RSedjl7/97e3d23yo/Doa/m++vTaf//w/O4Z6nhh9eQvlcRzq297Hh6yP/10F//7urXFjoN7zGK7N+vB1TPUPh3Dv/9orCDOv6fmy2JfT8OdZe2eH87vWb3Hh9S2oeqB09ng/BVA4fTu/ktnOb+264Pv7s96yi/xmPuwtgfFVN5+35naT+vMzxw/j+YWst/nNyc4PX4eTjwO2ezzb+HqDAZi2/gB9WL/98b8AZkbs4BsvAAA= -->
