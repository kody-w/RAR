---
name: "rar-cowork-cookbook-pricing-screenshot-to-customer-presentation"
description: "Turn an approved pricing screenshot into a customer-ready deck - numbers exact, deck polished, email drafted."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/pricing_screenshot_to_customer_presentation", "rar_sha256": "a95931c5b1c78d2d63b5e4f21dcea810974298609fe10f21360b8b4c8b8f2054", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "pricing_screenshot_to_customer_presentation_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/pricing-screenshot-to-customer-presentation:a55c5200cfe7326f189ca313aacf0b626b7f1d847dd4db6e44dbe97f36eb40c7", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "intermediate", "read_only"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/pricing_screenshot_to_customer_presentation`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `pricing_screenshot_to_customer_presentation_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

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
