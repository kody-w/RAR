---
name: "rar-cowork-cookbook-pricing-screenshot-to-customer-presentation"
description: "Turn an approved pricing screenshot into a customer-ready deck - numbers exact, deck polished, email drafted."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/pricing_screenshot_to_customer_presentation", "rar_sha256": "a95931c5b1c78d2d63b5e4f21dcea810974298609fe10f21360b8b4c8b8f2054", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "intermediate", "read_only"]}
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

Pricing screenshot -> customer presentation — Turn an approved pricing screenshot into a customer-ready deck - numbers exact, deck polished, email drafted.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

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
    "audience": {
      "description": "Optional. Who reads it \u2014 this drives register, length and what can be assumed.",
      "type": "string"
    },
    "operation": {
      "description": "What to do: run, plan, checklist, describe.",
      "enum": [
        "run",
        "plan",
        "checklist",
        "describe"
      ],
      "type": "string"
    },
    "subject": {
      "description": "What to produce, and about what.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `pricing_screenshot_to_customer_presentation_agent.py` and embedded as the fenced Python below (sha256 a95931c5b1c78d2d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `pricing_screenshot_to_customer_presentation_agent.py` first:

```bash
python3 pricing_screenshot_to_customer_presentation_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 pricing_screenshot_to_customer_presentation_agent.py   # or on stdin
python3 pricing_screenshot_to_customer_presentation_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Pricing screenshot -> customer presentation — Turn an approved pricing screenshot into a customer-ready deck - numbers exact, deck polished, email drafted.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

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
    "version": '2.0.0',
    "display_name": 'Pricing screenshot -> customer presentation',
    "description": 'Turn an approved pricing screenshot into a customer-ready deck - numbers exact, deck polished, email drafted.',
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
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '02b82b73fd7ca9e4',
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


# The toasted capability. The upstream entry supplies the WHAT; this procedure
# is RAR's own method for that shape of work, generated by
# @kody-w/skill_toaster_agent from the metadata we hold. No upstream text is
# reproduced here — see the module docstring.
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.5, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['word:deck'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class PricingScreenshotToCustomerPresentation(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PricingScreenshotToCustomerPresentation'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'audience': {'description': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What to produce, and about what.', 'type': 'string'}},
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

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

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
