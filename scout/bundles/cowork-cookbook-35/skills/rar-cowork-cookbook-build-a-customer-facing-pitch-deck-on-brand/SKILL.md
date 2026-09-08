---
name: "rar-cowork-cookbook-build-a-customer-facing-pitch-deck-on-brand"
description: "Returns a customer-facing pitch deck built on the approved Templafy corporate template for a named customer and executive audience, grounded in release messaging, recent customer email/meeting context, and battlecards, t"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/build_a_customer_facing_pitch_deck_on_brand", "rar_sha256": "1fb3baaa7faf775a0523f1b02bee087eb0e88e7d369e455fa101e33bb622aafd", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "concept_to_market", "beginner", "read_only"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/build_a_customer_facing_pitch_deck_on_brand`. The original RAPP
agent is preserved byte-for-byte in `build_a_customer_facing_pitch_deck_on_brand_agent.py` and in the RCI capsule.

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

Build a customer-facing pitch deck on brand — Returns a customer-facing pitch deck built on the approved Templafy corporate template for a named customer and executive audience, grounded in release messaging, recent customer email/meeting context, and battlecards, t

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
  Upstream entry : https://coworkcookbook.com/recipes/build-a-customer-facing-pitch-deck-on-brand
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
    "battlecard_folder": {
      "description": "Folder of battlecards used for competitive framing.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "customer_name": {
      "description": "The customer account the deck is built for.",
      "type": "string"
    },
    "executive_audience": {
      "description": "The enterprise exec audience the deck is tailored to (e.g. CFO, CIO).",
      "type": "string"
    },
    "messaging_doc": {
      "description": "Source doc holding the latest release positioning.",
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
    "platform_or_release": {
      "description": "The platform or release the deck introduces.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `build_a_customer_facing_pitch_deck_on_brand_agent.py` and embedded as the fenced Python below (sha256 1fb3baaa7faf775a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `build_a_customer_facing_pitch_deck_on_brand_agent.py` first:

```bash
python3 build_a_customer_facing_pitch_deck_on_brand_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 build_a_customer_facing_pitch_deck_on_brand_agent.py   # or on stdin
python3 build_a_customer_facing_pitch_deck_on_brand_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Build a customer-facing pitch deck on brand — Returns a customer-facing pitch deck built on the approved Templafy corporate template for a named customer and executive audience, grounded in release messaging, recent customer email/meeting context, and battlecards, t

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
  Upstream entry : https://coworkcookbook.com/recipes/build-a-customer-facing-pitch-deck-on-brand
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/build_a_customer_facing_pitch_deck_on_brand',
    "version": '3.0.3',
    "display_name": 'Build a customer-facing pitch deck on brand',
    "description": 'Returns a customer-facing pitch deck built on the approved Templafy corporate template for a named customer and executive audience, grounded in release messaging, recent customer email/meeting context, and battlecards, t',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'concept_to_market', 'beginner', 'read_only'],
    "category": 'general',
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
        "upstream_slug": 'build-a-customer-facing-pitch-deck-on-brand',
        "upstream_url": 'https://coworkcookbook.com/recipes/build-a-customer-facing-pitch-deck-on-brand',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b6997b7f8cd858d1',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'beginner', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'none', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/prepare-marketing-campaigns/create-marketing-material'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/build-a-customer-facing-pitch-deck-on-brand', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Email', 'Meetings', 'Communications'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Microsoft 365 Copilot licence with access to Cowork', "Output matches: A Templafy pitch deck for an enterprise audience - grounded in the platform release messaging and the customer's strategic context - built on approved corporate templates so the field can lead with it."], 'confidence': 1.0, 'deliverable': "A Templafy pitch deck for an enterprise audience - grounded in the platform release messaging and the customer's strategic context - built on approved corporate templates so the field can lead with it.", 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'battlecard_folder': 'Folder of battlecards used for competitive framing.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'customer_name': 'The customer account the deck is built for.', 'executive_audience': 'The enterprise exec audience the deck is tailored to (e.g. CFO, CIO).', 'messaging_doc': 'Source doc holding the latest release positioning.', 'platform_or_release': 'The platform or release the deck introduces.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Hand the field a customer-facing pitch deck that's on-brand, on-message, and tailored to a specific exec audience - instead of letting every team rebuild from a generic template. A Templafy pitch deck for an enterprise audience - grounded in the platform release messaging and the customer's strategic context - built on approved corporate templates so the field can lead with it.", 'expected_output': "A Templafy pitch deck for an enterprise audience - grounded in the platform release messaging and the customer's strategic context - built on approved corporate templates so the field can lead with it.", 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Microsoft 365 Copilot licence with access to Cowork'], 'prompt': 'Build a customer-facing pitch deck introducing our new [Platform/Release] for an enterprise [Executive audience] at [Customer name]. Pull the latest release positioning from [Messaging doc], customer-specific context from recent emails and meetings, and competitive framing from [Battlecard folder].\n\nUse Templafy to apply our approved corporate template.\n\nStructure: cover · why now · platform overview · audience value · proof + customer outcomes · differentiation · next steps.\n\nRoute the draft to my manager for a final pass on positioning and stakeholder fit.', 'steps': ['Open Cowork and start a new task.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': "A Templafy pitch deck for an enterprise audience - grounded in the platform release messaging and the customer's strategic context - built on approved corporate templates so the field can lead with it."}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Returns a customer-facing pitch deck built on the approved Templafy corporate template for a named customer and executive audience, grounded in release messaging, recent customer email/meeting context, and battlecards, t', 'example_request': 'Build a CIO pitch deck for Contoso on our new Fabric release using the Q3 messaging doc and battlecards.', 'inputs': [{'description': 'The platform or release the deck introduces.', 'name': 'platform_or_release'}, {'description': 'The enterprise exec audience the deck is tailored to (e.g. CFO, CIO).', 'name': 'executive_audience'}, {'description': 'The customer account the deck is built for.', 'name': 'customer_name'}, {'description': 'Source doc holding the latest release positioning.', 'name': 'messaging_doc'}, {'description': 'Folder of battlecards used for competitive framing.', 'name': 'battlecard_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when the field needs an on-brand, audience-tailored pitch deck for a platform or release at a specific enterprise customer instead of a generic template.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and start a new task.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BuildACustomerFacingPitchDeckOnBrand(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BuildACustomerFacingPitchDeckOnBrand'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'battlecard_folder': {'description': 'Folder of battlecards used for competitive framing.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'customer_name': {'description': 'The customer account the deck is built for.', 'type': 'string'}, 'executive_audience': {'description': 'The enterprise exec audience the deck is tailored to (e.g. CFO, CIO).', 'type': 'string'}, 'messaging_doc': {'description': 'Source doc holding the latest release positioning.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'platform_or_release': {'description': 'The platform or release the deck introduces.', 'type': 'string'}},
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
    print(BuildACustomerFacingPitchDeckOnBrand().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
