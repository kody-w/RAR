---
name: "rar-cowork-cookbook-report-manage-product-pricing"
description: "Builds a structured summary report of manage product pricing activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_manage_product_pricing", "rar_sha256": "9585da349888a15228ea33495825659b382b9a93bb393d5c567df9e7643ef1e9", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_manage_product_pricing_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-manage-product-pricing:17f2841f2f043c80f3d315e5afe715f83ede7dc709c1ba3b9fab6515d8aa77b7", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_manage_product_pricing`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_manage_product_pricing_agent.py` is
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
