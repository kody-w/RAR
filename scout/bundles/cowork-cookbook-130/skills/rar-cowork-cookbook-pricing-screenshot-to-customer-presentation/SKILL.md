---
name: "rar-cowork-cookbook-pricing-screenshot-to-customer-presentation"
description: "Turn an approved pricing screenshot into a customer-ready deck - numbers exact, deck polished, email drafted."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/pricing_screenshot_to_customer_presentation", "rar_sha256": "3d7a8183a0c50ca1080847438247b5581cfa215dcabd4c27ba6901320cfd3fca", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "intermediate", "read_only"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `pricing_screenshot_to_customer_presentation_agent.py` and embedded as the fenced Python below (sha256 3d7a8183a0c50ca1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `pricing_screenshot_to_customer_presentation_agent.py` first:

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
    "version": '2.0.1',
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
