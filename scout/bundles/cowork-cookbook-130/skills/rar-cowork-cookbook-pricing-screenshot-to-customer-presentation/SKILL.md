---
name: "rar-cowork-cookbook-pricing-screenshot-to-customer-presentation"
description: "Turns an approved pricing screenshot into a customer-ready PowerPoint deck (cover, context, exact pricing breakdown, next steps) plus a draft email to the contact, with the pricing slide shown for approval first."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/pricing_screenshot_to_customer_presentation", "rar_sha256": "263539c3d99e992167d4d3b2b3e817260364df031e4b7109ef0cd0aaeda0aa1b", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "intermediate", "read_only"]}
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
