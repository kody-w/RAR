---
name: "rar-cowork-cookbook-product-launch-customer-pitch"
description: "Produces a three-artifact competitive pitch kit for a customer meeting: an Excel comparison of your product vs. a competitor product, a Word value prop doc, and a customer-ready PowerPoint deck."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/product_launch_customer_pitch", "rar_sha256": "acdc04faaeb09554c47c29590a085741c1bf0da7a8bce798aecbe7eeb796bd8e", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "advanced", "read_only"]}
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
