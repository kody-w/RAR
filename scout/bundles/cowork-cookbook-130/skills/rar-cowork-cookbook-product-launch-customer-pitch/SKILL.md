---
name: "rar-cowork-cookbook-product-launch-customer-pitch"
description: "Produces a three-artifact competitive pitch kit for a customer meeting: an Excel comparison of your product vs. a competitor product, a Word value prop doc, and a customer-ready PowerPoint deck."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/product_launch_customer_pitch", "rar_sha256": "acdc04faaeb09554c47c29590a085741c1bf0da7a8bce798aecbe7eeb796bd8e", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "advanced", "read_only"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/product_launch_customer_pitch`. The original RAPP
agent is preserved byte-for-byte in `product_launch_customer_pitch_agent.py` and in the RCI capsule.

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

Product launch customer pitch — Produces a three-artifact competitive pitch kit for a customer meeting: an Excel comparison of your product vs. a competitor product, a Word value prop doc, and a customer-ready PowerPoint deck.

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
  Upstream entry : https://coworkcookbook.com/recipes/product-launch-customer-pitch
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
    "competitor_product": {
      "description": "The competitor product just announced that you need to differentiate against.",
      "type": "string"
    },
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
    "product": {
      "description": "Your product being positioned in the pitch.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `product_launch_customer_pitch_agent.py` and embedded as the fenced Python below (sha256 acdc04faaeb09554…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `product_launch_customer_pitch_agent.py` first:

```bash
python3 product_launch_customer_pitch_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 product_launch_customer_pitch_agent.py   # or on stdin
python3 product_launch_customer_pitch_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Product launch customer pitch — Produces a three-artifact competitive pitch kit for a customer meeting: an Excel comparison of your product vs. a competitor product, a Word value prop doc, and a customer-ready PowerPoint deck.

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
  Upstream entry : https://coworkcookbook.com/recipes/product-launch-customer-pitch
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/product_launch_customer_pitch',
    "version": '3.0.3',
    "display_name": 'Product launch customer pitch',
    "description": 'Produces a three-artifact competitive pitch kit for a customer meeting: an Excel comparison of your product vs. a competitor product, a Word value prop doc, and a customer-ready PowerPoint deck.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'prospect_to_quote', 'advanced', 'read_only'],
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
        "upstream_slug": 'product-launch-customer-pitch',
        "upstream_url": 'https://coworkcookbook.com/recipes/product-launch-customer-pitch',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ddb75d72e477afad',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'advanced', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'none', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/pursue-opportunities/nurture-opportunities-and-finalize-the-sale'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/product-launch-customer-pitch', 'uses_skills': {'custom': [], 'ootb': ['Word', 'Excel', 'PowerPoint', 'Meetings', 'Communications'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Microsoft 365 Copilot licence with access to Cowork', "Output matches: An Excel competitive comparison, a Word value prop document, and a customer-ready PowerPoint pitch deck - a three-artifact kit ready for tomorrow's meeting."], 'confidence': 1.0, 'deliverable': "An Excel competitive comparison, a Word value prop document, and a customer-ready PowerPoint pitch deck - a three-artifact kit ready for tomorrow's meeting.", 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'competitor_product': 'The competitor product just announced that you need to differentiate against.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'product': 'Your product being positioned in the pitch.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Turn a competitor announcement into a sharp, differentiated customer pitch - built and ready before tomorrow's meeting. An Excel competitive comparison, a Word value prop document, and a customer-ready PowerPoint pitch deck - a three-artifact kit ready for tomorrow's meeting.", 'expected_output': "An Excel competitive comparison, a Word value prop document, and a customer-ready PowerPoint pitch deck - a three-artifact kit ready for tomorrow's meeting.", 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Microsoft 365 Copilot licence with access to Cowork'], 'prompt': "I have a customer meeting tomorrow and need a sharp competitive pitch for [Product]. Our competitor just announced [Competitor Product] - I need to position [Product] distinctly.\n\nStart with a consultant-level comparison between [Product] and [Competitor Product] - put it in an Excel with clear differentiation across the dimensions that matter most.\n\nThen build a value prop document focused entirely on [Product]: what makes it compelling, how it stands apart from our own portfolio, and why it's the right choice for this customer. Keep the language direct and easy to read - not marketing-heavy.\n\nFinally, bring it all together in a customer-ready PowerPoint pitch deck I can present tomorrow.", 'steps': ['Open Cowork and start a new task.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': "An Excel competitive comparison, a Word value prop document, and a customer-ready PowerPoint pitch deck - a three-artifact kit ready for tomorrow's meeting."}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Produces a three-artifact competitive pitch kit for a customer meeting: an Excel comparison of your product vs. a competitor product, a Word value prop doc, and a customer-ready PowerPoint deck.', 'example_request': 'Competitor announced Acme Flow — build me a comparison sheet, value prop doc, and pitch deck for Contoso Sync by tomorrow.', 'inputs': [{'description': 'Your product being positioned in the pitch.', 'name': 'product'}, {'description': 'The competitor product just announced that you need to differentiate against.', 'name': 'competitor_product'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a competitor has announced a product and you need a differentiated pitch for an upcoming customer meeting.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and start a new task.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ProductLaunchCustomerPitch(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ProductLaunchCustomerPitch'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'competitor_product': {'description': 'The competitor product just announced that you need to differentiate against.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'product': {'description': 'Your product being positioned in the pitch.', 'type': 'string'}},
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
    print(ProductLaunchCustomerPitch().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
