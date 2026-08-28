---
name: "rar-cowork-cookbook-report-manage-product-pricing"
description: "Builds a structured summary report of manage product pricing activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_manage_product_pricing", "rar_sha256": "56299b93ad250340c3acd1d2bf851cff1218913960f12e73d4fa95dd649dfba8", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_manage_product_pricing_agent.py` and embedded as the fenced Python below (sha256 56299b93ad250340…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_manage_product_pricing_agent.py` first:

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
    "version": '2.0.1',
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
