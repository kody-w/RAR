---
name: "rar-cowork-cookbook-build-a-customer-facing-pitch-deck-on-brand"
description: "Returns a customer-facing pitch deck built on the approved Templafy corporate template for a named customer and executive audience, grounded in release messaging, recent customer email/meeting context, and battlecards, t"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/build_a_customer_facing_pitch_deck_on_brand", "rar_sha256": "1fb3baaa7faf775a0523f1b02bee087eb0e88e7d369e455fa101e33bb622aafd", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "concept_to_market", "beginner", "read_only"]}
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
