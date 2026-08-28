---
name: "rar-cowork-cookbook-report-develop-product-catalogs"
description: "Builds a structured summary report of develop product catalogs activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_develop_product_catalogs", "rar_sha256": "8bdf74617a5e43c0eb6edeb1d2ffbc9d1d6920bf0d138b5f6b9f0c1a8544cc99", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_develop_product_catalogs`. The original RAPP
agent is preserved byte-for-byte in `report_develop_product_catalogs_agent.py` and in the RCI capsule.

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

Develop product catalogs Summary Report — Builds a structured summary report of develop product catalogs activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-develop-product-catalogs
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_develop_product_catalogs_agent.py` and embedded as the fenced Python below (sha256 8bdf74617a5e43c0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_develop_product_catalogs_agent.py` first:

```bash
python3 report_develop_product_catalogs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_develop_product_catalogs_agent.py   # or on stdin
python3 report_develop_product_catalogs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop product catalogs Summary Report — Builds a structured summary report of develop product catalogs activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-develop-product-catalogs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_develop_product_catalogs',
    "version": '2.0.0',
    "display_name": 'Develop product catalogs Summary Report',
    "description": 'Builds a structured summary report of develop product catalogs activity with totals, trends, and breakdowns.',
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
        "upstream_slug": 'report-develop-product-catalogs',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-develop-product-catalogs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '222e272cc622cf3d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/develop-product-strategy/develop-product-catalogs'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/report-develop-product-catalogs', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportDevelopProductCatalogs(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportDevelopProductCatalogs'
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
    print(ReportDevelopProductCatalogs().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
