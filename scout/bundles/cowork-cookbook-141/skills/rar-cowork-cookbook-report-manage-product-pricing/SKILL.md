---
name: "rar-cowork-cookbook-report-manage-product-pricing"
description: "Builds a structured summary report of manage product pricing activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_manage_product_pricing", "rar_sha256": "9585da349888a15228ea33495825659b382b9a93bb393d5c567df9e7643ef1e9", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_manage_product_pricing`. The original RAPP
agent is preserved byte-for-byte in `report_manage_product_pricing_agent.py` and in the RCI capsule.

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

Manage product pricing Summary Report — Builds a structured summary report of manage product pricing activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-manage-product-pricing
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_manage_product_pricing_agent.py` and embedded as the fenced Python below (sha256 9585da349888a152…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_manage_product_pricing_agent.py` first:

```bash
python3 report_manage_product_pricing_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_manage_product_pricing_agent.py   # or on stdin
python3 report_manage_product_pricing_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage product pricing Summary Report — Builds a structured summary report of manage product pricing activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-manage-product-pricing
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_manage_product_pricing',
    "version": '2.0.0',
    "display_name": 'Manage product pricing Summary Report',
    "description": 'Builds a structured summary report of manage product pricing activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-manage-product-pricing',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-manage-product-pricing',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b9ce008e0a9bcc46',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/manage-active-products/manage-product-pricing'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/report-manage-product-pricing', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.333, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:report'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class ReportManageProductPricing(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportManageProductPricing'
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
    print(ReportManageProductPricing().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
