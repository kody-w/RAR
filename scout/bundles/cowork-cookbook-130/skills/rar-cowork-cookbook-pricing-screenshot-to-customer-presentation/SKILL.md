---
name: "rar-cowork-cookbook-pricing-screenshot-to-customer-presentation"
description: "Turns an approved pricing screenshot into a customer-ready PowerPoint deck (cover, context, exact pricing breakdown, next steps) plus a draft email to the contact, with the pricing slide shown for approval first."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/pricing_screenshot_to_customer_presentation", "rar_sha256": "263539c3d99e992167d4d3b2b3e817260364df031e4b7109ef0cd0aaeda0aa1b", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "intermediate", "read_only"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/pricing_screenshot_to_customer_presentation`. The original RAPP
agent is preserved byte-for-byte in `pricing_screenshot_to_customer_presentation_agent.py` and in the RCI capsule.

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

Pricing screenshot -> customer presentation — Turns an approved pricing screenshot into a customer-ready PowerPoint deck (cover, context, exact pricing breakdown, next steps) plus a draft email to the contact, with the pricing slide shown for approval first.

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
  Upstream entry : https://coworkcookbook.com/recipes/pricing-screenshot-to-customer-presentation
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
    "company_name": {
      "description": "Customer company name for the cover slide.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "customer_contact_name": {
      "description": "Person the draft email attaching the deck is addressed to.",
      "type": "string"
    },
    "meeting_date": {
      "description": "Date of the customer meeting, shown on the cover slide.",
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
    "pricing_screenshot": {
      "description": "Screenshot image of the approved pricing for the product; figures must be reproduced exactly.",
      "type": "string"
    },
    "product": {
      "description": "Name of the product the approved pricing covers.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `pricing_screenshot_to_customer_presentation_agent.py` and embedded as the fenced Python below (sha256 263539c3d99e9921…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `pricing_screenshot_to_customer_presentation_agent.py` first:

```bash
python3 pricing_screenshot_to_customer_presentation_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 pricing_screenshot_to_customer_presentation_agent.py   # or on stdin
python3 pricing_screenshot_to_customer_presentation_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Pricing screenshot -> customer presentation — Turns an approved pricing screenshot into a customer-ready PowerPoint deck (cover, context, exact pricing breakdown, next steps) plus a draft email to the contact, with the pricing slide shown for approval first.

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
  Upstream entry : https://coworkcookbook.com/recipes/pricing-screenshot-to-customer-presentation
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/pricing_screenshot_to_customer_presentation',
    "version": '3.0.3',
    "display_name": 'Pricing screenshot -> customer presentation',
    "description": 'Turns an approved pricing screenshot into a customer-ready PowerPoint deck (cover, context, exact pricing breakdown, next steps) plus a draft email to the contact, with the pricing slide shown for approval first.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'prospect_to_quote', 'intermediate', 'read_only'],
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
        "upstream_slug": 'pricing-screenshot-to-customer-presentation',
        "upstream_url": 'https://coworkcookbook.com/recipes/pricing-screenshot-to-customer-presentation',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '54e129e4637049af',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'none', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/estimate-and-quote-sales/define-sales-quotations'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/pricing-screenshot-to-customer-presentation', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Email', 'Meetings'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Microsoft 365 Copilot licence with access to Cowork', 'Output matches: A customer-ready PowerPoint deck (cover, context, pricing, next steps) and a draft customer email with the deck attached - pricing slide surfaced for your approval before the rest of the deck is built.'], 'confidence': 1.0, 'deliverable': 'A customer-ready PowerPoint deck (cover, context, pricing, next steps) and a draft customer email with the deck attached - pricing slide surfaced for your approval before the rest of the deck is built.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'company_name': 'Customer company name for the cover slide.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'customer_contact_name': 'Person the draft email attaching the deck is addressed to.', 'meeting_date': 'Date of the customer meeting, shown on the cover slide.', 'pricing_screenshot': 'Screenshot image of the approved pricing for the product; figures must be reproduced exactly.', 'product': 'Name of the product the approved pricing covers.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Turn an approved pricing screenshot into a customer-ready deck - numbers exact, deck polished, email drafted. A customer-ready PowerPoint deck (cover, context, pricing, next steps) and a draft customer email with the deck attached - pricing slide surfaced for your approval before the rest of the deck is built.', 'expected_output': 'A customer-ready PowerPoint deck (cover, context, pricing, next steps) and a draft customer email with the deck attached - pricing slide surfaced for your approval before the rest of the deck is built.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Microsoft 365 Copilot licence with access to Cowork'], 'prompt': 'I have a customer meeting on [Meeting Date] and just received final pricing approval from finance. This is a screenshot of approved pricing for [Product]. Use this to create a customer-ready presentation I can share. Do not alter any numbers - they must be accurately represented in the output.\n\nBefore completing the full deck, show me the pricing slide first for review.\n\nOnce confirmed, build out the full presentation with:\n\nA brief cover slide with [Company Name] and meeting date\n\nA context slide framing the offer (pull from any prior emails or files about this account if available)\n\nThe pricing breakdown slide - exact figures, no rounding or paraphrasing\n\nA next steps slide with placeholder actions we can fill in together\n\nWhen the deck is ready, draft a short email to [Customer Contact Name] attaching the presentation, and flag if anything in the pricing image was unclear or ambiguous before I send.', 'steps': ['Open Cowork and start a new task.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'A customer-ready PowerPoint deck (cover, context, pricing, next steps) and a draft customer email with the deck attached - pricing slide surfaced for your approval before the rest of the deck is built.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Turns an approved pricing screenshot into a customer-ready PowerPoint deck (cover, context, exact pricing breakdown, next steps) plus a draft email to the contact, with the pricing slide shown for approval first.', 'example_request': "Here's the approved pricing screenshot for Contoso Cloud - build a deck for my Mar 12 meeting with Acme and draft the email to Dana.", 'inputs': [{'description': 'Screenshot image of the approved pricing for the product; figures must be reproduced exactly.', 'name': 'pricing_screenshot'}, {'description': 'Date of the customer meeting, shown on the cover slide.', 'name': 'meeting_date'}, {'description': 'Name of the product the approved pricing covers.', 'name': 'product'}, {'description': 'Customer company name for the cover slide.', 'name': 'company_name'}, {'description': 'Person the draft email attaching the deck is addressed to.', 'name': 'customer_contact_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you have a finance-approved pricing screenshot for a product and need a customer meeting deck and draft email with figures reproduced exactly.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and start a new task.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PricingScreenshotToCustomerPresentation(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PricingScreenshotToCustomerPresentation'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'company_name': {'description': 'Customer company name for the cover slide.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'customer_contact_name': {'description': 'Person the draft email attaching the deck is addressed to.', 'type': 'string'}, 'meeting_date': {'description': 'Date of the customer meeting, shown on the cover slide.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'pricing_screenshot': {'description': 'Screenshot image of the approved pricing for the product; figures must be reproduced exactly.', 'type': 'string'}, 'product': {'description': 'Name of the product the approved pricing covers.', 'type': 'string'}},
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
    print(PricingScreenshotToCustomerPresentation().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
