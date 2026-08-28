---
name: "rar-cowork-cookbook-report-develop-product-catalogs"
description: "Builds a structured summary report of develop product catalogs activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_develop_product_catalogs", "rar_sha256": "1fd5c5b38c4983cbb53302ffe1bf5bf48dd404ff08fefb270075f38d267e9b31", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_develop_product_catalogs_agent.py` and embedded as the fenced Python below (sha256 1fd5c5b38c4983cb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_develop_product_catalogs_agent.py` first:

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
    "version": '2.0.1',
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
