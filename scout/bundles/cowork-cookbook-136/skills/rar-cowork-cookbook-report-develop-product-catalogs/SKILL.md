---
name: "rar-cowork-cookbook-report-develop-product-catalogs"
description: "Builds a structured summary report of develop product catalogs activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_develop_product_catalogs", "rar_sha256": "8bdf74617a5e43c0eb6edeb1d2ffbc9d1d6920bf0d138b5f6b9f0c1a8544cc99", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_develop_product_catalogs_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-develop-product-catalogs:0b2294170f67935278443912b2a84be31441de34279ec5d4daf2df7f5eb23744", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_develop_product_catalogs`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_develop_product_catalogs_agent.py` is
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
