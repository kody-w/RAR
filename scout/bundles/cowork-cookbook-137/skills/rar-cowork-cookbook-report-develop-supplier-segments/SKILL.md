---
name: "rar-cowork-cookbook-report-develop-supplier-segments"
description: "Builds a structured summary report of develop supplier segments activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_develop_supplier_segments", "rar_sha256": "eb94c034f8b27e77c37de0219da5338a32141909618bdf1d22dbb522910f2070", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_develop_supplier_segments_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-develop-supplier-segments:2db53583f454960690404e49bd021ebf3ddea520225ecb7657d0865291f1fcae", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_develop_supplier_segments`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_develop_supplier_segments_agent.py` is
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

Develop supplier segments Summary Report — Builds a structured summary report of develop supplier segments activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-develop-supplier-segments
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_develop_supplier_segments_agent.py` and embedded as the fenced Python below (sha256 eb94c034f8b27e77…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_develop_supplier_segments_agent.py` first:

```bash
python3 report_develop_supplier_segments_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_develop_supplier_segments_agent.py   # or on stdin
python3 report_develop_supplier_segments_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop supplier segments Summary Report — Builds a structured summary report of develop supplier segments activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-develop-supplier-segments
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_develop_supplier_segments',
    "version": '2.0.0',
    "display_name": 'Develop supplier segments Summary Report',
    "description": 'Builds a structured summary report of develop supplier segments activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-develop-supplier-segments',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-develop-supplier-segments',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4c0a665999e95fbd',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/develop-procurement-and-sourcing-strategy/develop-supplier-segments'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/report-develop-supplier-segments', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportDevelopSupplierSegments(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportDevelopSupplierSegments'
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
    print(ReportDevelopSupplierSegments().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
